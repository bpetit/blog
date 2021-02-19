---
title: "Automating web applications proxying, DNS registration and TLS termination with ansible"
tags:
  - automation
  - cd
  - ansible
  - dns
  - letsencrypt
  - knot
  - tls
date: 2018-03-17T20:12:45+02:00
author: Benoit Petit
---

For the needs of an incoming project, that I'll describe in a later post, I needed to automate public access configuration for existing web applications. In other words, I needed to automate, proxy vhost configuration, tls termination and dns registration on a given domain. What is presented here has been used on a simple libvirt/KVM architecture (managed as described in my latest post).

The workflow is this one:

+ deploy the DNS entry
+ deploy nginx vhost for the given webapp and domain name (allowing access to .well-known directory for letsencrypt http based authentication and authorization)
+ ask for letsencrypt certificate
+ retrieve certificate and configure tcp/443 vhost with tls

Here are the components I used:

+ nginx: the well known reverse proxy and web server
+ letsencrypt: the tls certificates delivering authority and API
+ knot DNS: as an authoritative DNS server on my base domain name
+ ansible: to deploy everything

The following setup is a proof of concept. It surely has flaws and will be improved later. As always, I'd be really happy to read your tips or hints for improvement in the comments.

## 1. Automating DNS configuration

All configurations seen here are ansible (yaml) playbooks and variables files. That being said, configuration templates can be, after small changes, used to configure an equivalent setup manually (but this has no interest in my case).

As specified earlier, I choosed knot DNS to do the job. This DNS (authoritative only) server is famous for its performances. It is also very easy to configure. To deploy and configure knot with ansible I used an existing role. Here is my fork: https://github.com/bpetit/ansible-role-knotauth (I definitely have to make a PR and try to resynchronize with upstream, this is on my todo). Basically the role worked very well from the beginning to install knot and deploy basic configuration. All I wanted in addition was to be able to deploy zone files from ansible.

I don't detail the initial and necessary part, which was about registering my domain to a registrar and specify my DNS server as the first authoritative DNS server of the domain.

Let's have a look to the way the role has to be called:

{{< highlight yaml >}}
- hosts: dns
  roles:
    - knot
{{</ highlight >}}

This is as simple as that, but it is required to fill variables for the role in the host vars file of the dns server:

{{< highlight yaml >}}
############################
## knot DNS configuration

knot_user: knot
knot_group: knot
knot_interfaces:
  - 127.0.0.1
  - "{{ ansible_default_ipv4.address }}"
knot_zones:
  - { name: 'nc42.fr', storage: "{{ knot_install_dir }}/etc/knot/zones", file: "nc42.fr.zone", src_file: 'files/nc42.fr.zone' }
{{</ highlight >}}

And the zone file looks like this (currently, this is a file, but will be a template in next commits):

{{< highlight bash >}}
$TTL 1

$ORIGIN nc42.fr.
nc42.fr. 600 IN SOA ns1.nc42.fr. (
  hostmaster.nc42.fr.
  2018021801
  86400
  7200
  604800
  86400
)

$TTL 86400

@       NS      ns1.nc42.fr.
@       NS      ns2.nc42.fr.

mysuperapp     A    192.0.2.3
mysuperapp2     A   192.0.2.4
mysuperapp3     A   192.0.2.5
{{</ highlight >}}

For now, I need to edit the zone file each time I need to create a new domain name and rerun the ansible playbook. This is ok, but will be improved with a template, using host vars.

## 2. Nginx proxy configuration and webroot setup for LE http validation

Now we need to configure the nginx vhost that will:

+ serve the files used by letsencrypt to validate the domain
+ behave as a proxy for the application behind
+ permit the tls encryption of the communication with the clients

Let's see what we have in `host_vars/proxy1`:

{{< highlight bash >}}
webroot: /var/www

domains:
  - { "name": "myapp3.nc42.fr", "renew": True, "template": "templates/nginx_vhost.j2" }

nginx_templatized_vhosts: "{{ domains }}"

letsencrypt_path: /etc/letsencrypt/live

nginx_delete_default_site: True
{{</ highlight >}}

Here is the template `nginx_vhosts.j2`:

{{< highlight jinja >}}
server {
    listen 80;
    listen [::]:80;
    server_name {{ item.name }} ;
    access_log /var/log/nginx/{{ item.name }}_access.log;
    error_log /var/log/nginx/{{ item.name }}_error.log;
    root /var/www/{{ item.name }};
    location / {
        rewrite ^/(.*)$ https://$host$request_uri;
    }
    location /.well-known/acme-challenge/ {
        alias /var/www/{{ item.name }}/.well-known/acme-challenge/;
        allow all;
    }
}
server {
    listen 443;
    listen [::]:443;
    server_name {{ item.name }};
    access_log /var/log/nginx/{{ item.name }}_access.log;
    error_log /var/log/nginx/{{ item.name }}_error.log;
    ssl on;
    ssl_certificate {{ letsencrypt_path }}/{{ item.name }}/{{ item.name }}.crt;
    ssl_certificate_key {{ letsencrypt_path }}/{{ item.name }}/{{ item.name }}.key;
    ssl_protocols      TLSv1.1 TLSv1.2;
    ssl_ciphers kEECDH+ECDSA:kEECDH:kEDH:HIGH:SHA256:!RC4:!aNULL:!eNULL:!LOW:!3DES:!MD5:!EXP:!DSS:!PSK:!SRP:!CAMELLIA;
    ssl_prefer_server_ciphers on;
    location /.well-known/acme-challenge/ {
        alias /var/www/{{ item.name }}/.well-known/acme-challenge/;
        allow all;
    }

    # TODO: proxy configuration

    root {{ webroot }}/{{ item.name }};
}
{{</ highlight >}}

Here's what the beginning of the playbook looks like:

{{< highlight yaml >}}
- hosts: proxy
  pre_tasks:
    - name: ensure web directories exist (1)
      file:
        state: directory
        path: "{{ webroot }}/{{ item.name }}"
        owner: www-data
        group: www-data
      with_items:
        - "{{ domains }}"
    - name: ensure letsencrypt paths exists (2)
      file:
        state: directory
        path: "{{ letsencrypt_path }}/{{ item.name }}"
      with_items:
        - "{{ domains }}"
    - name: prepare tls private keys (3)
      shell: "! [ -e {{ letsencrypt_path }}/{{ item.name }}/{{ item.name }}.key ] && openssl genrsa -out {{ letsencrypt_path }}/{{ item.name }}/{{ item.name }}.key 4096"
      with_items:
        - "{{ domains }}"
      ignore_errors: True
    - name: prepare account keys (4)
      shell: "! [ -e {{ letsencrypt_path }}/{{ item.name }}/{{ item.name }}_account.key ] && openssl genrsa -out {{ letsencrypt_path }}/{{ item.name }}/{{ item.name }}_account.key 4096"
      with_items:
        - "{{ domains }}"
      ignore_errors: True
    - name: prepare tls CSRs (5)
      shell: "openssl req -new -key {{ letsencrypt_path }}/{{ item.name }}/{{ item.name }}.key -subj \"/C=FR/ST=IDF/L=Paris/O=arawbase.com/OU=Hosting services/CN={{ item.name }}\" -out {{ letsencrypt_path }}/{{ item.name }}/{{ item.name }}.csr"
      when: "item.renew is defined and item.renew"
      with_items:
        - "{{ domains }}"
    - name: generate auto-signed certificate if it doesn't exist (6)
      shell: "! [ -e {{ letsencrypt_path }}/{{ item.name }}/{{ item.name }}.crt ] && openssl x509 -req -days 365 -in {{ letsencrypt_path }}/{{ item.name }}/{{ item.name }}.csr -sign key {{ letsencrypt_path }}/{{ item.name }}/{{ item.name }}.key -out {{ letsencrypt_path }}/{{ item.name }}/{{ item.name }}.crt"
      with_items:
        - "{{ domains }}"
      ignore_errors: True
roles: # (7)
  - nginx
post_tasks:
  - service: # (8)
      name: nginx
      state: reloaded
{{</ highlight >}}

Let's detail whats going on here. First we write the list of our domains/applications to configure in the hosts vars file. For each item (dictionnary describing a domain) of this list, we will:

+ create the directory (webroot) dedicated to that domain on the proxy server, to store letsenrypt files (used for validation, not key/certificate files)
+ ensure the letsencrypt path for that domain exists, to store key and certificate files
+ generate a private key, using openssl (that part is stil a bit dirty, as we use the shell module which is not idempotent)
+ generate a provate key for the letsencrypt account (we need to generate seperate keys for the certificate generation and the account authentication, otherwise letsencrypt refuses the certificate validation)
+ generate the CSR (Certificate Signing Request) we will send to LE to get the final certificate
+ generate a self signed tls certificate, in order to permit to the nginx vhost to work until the LE certificate is retrieved
+ call the nginx role, that will install the software and configure the vhost base on the template we specified, we will see this in the next part
+ ensure nginx is reloaded to consider our changes

## 3. Nginx configuration

I use this role: https://github.com/bpetit/Stouts.nginx which is a fork (of https://github.com/Stouts/Stouts.nginx). Same as earlier, next steps include proposing a PR with my changes, and resynchronize with upstream. I only wanted to permit inclusion of external templates for vhost configurations. (Templates are called by the `nginx_templatized_vhosts` variable in the host vars file)

## 4. Letsencrypt validation and deployment

In the same main playbook I include a tasks file dedicated to this part, with the domain list as a parameter:

{{< highlight yaml >}}
- hosts: proxy
  tasks:
    - name: include letsencrypt tasks
      include_tasks: letsencrypt.yml
      with_items:
        - "{{ domains }}"
    - service:
        name: nginx
        state: reloaded
{{</ highlight >}}

Here is the included file:

{{< highlight yaml >}}
- name: ensure well-known directory exists (1)
  file:
    path: "{{ webroot }}/{{ item.name }}/.well-known/acme-challenge"
    state: directory
    recurse: yes
    owner: www-data
    group: www-data
- name: request letsencrypt for a challenge (2)
  letsencrypt:
    account_key: "{{ letsencrypt_path }}/{{ item.name }}/{{ item.name }}_account.key"
    csr: "{{ letsencrypt_path }}/{{ item.name }}/{{ item.name }}.csr"
    dest: "{{ letsencrypt_path }}/{{ item.name }}/{{ item.name }}.crt"
    agreement: https://letsencrypt.org/documents/LE-SA-v1.2-November-15-2017.pdf
    account_email: "bpetit@b0rk.in"
    remaining_days: 365
    #acme_directory: https://acme-v01.api.letsencrypt.org/directory
  register: le_challenge
  when: "item.renew is defined and item.renew"
- name: create the data of the challenge in a file on the webroot of the domain (3)
  copy:
    dest: "{{ webroot }}/{{ item.name }}/{{ le_challenge['challenge_data'][item.name]['http-01']['resource'] }}"
    content: "{{ le_challenge['challenge_data'][item.name]['http-01']['resource_value'] }}"
    owner: www-data
    group: www-data
  when: le_challenge|changed
- name: ask LE to create the certificate file and retrieve it (4)
  letsencrypt:
    account_key: "{{ letsencrypt_path }}/{{ item.name }}/{{ item.name }}_account.key"
    csr: "{{ letsencrypt_path }}/{{ item.name }}/{{ item.name }}.csr"
    dest: "{{ letsencrypt_path }}/{{ item.name }}/{{ item.name }}.crt"
    data: "{{ le_challenge }} "
    agreement: https://letsencrypt.org/documents/LE-SA-v1.2-November-15-2017.pdf
    account_email: "bpetit@b0rk.in"
    remaining_days: 365
    #acme_directory: https://acme-v01.api.letsencrypt.org/directory
  register: result
  when: "item.renew is defined and item.renew and le_challenge|changed"
{{</ highlight >}}

Let's detail the steps:

+ we check that the well-known folder exist in the webroot
+ we request LE for challenge data
+ challenge data is stored in a file (served by nginx, remember) that will be accessed by LE http validation service
+ we trigger the validation and retrieve the certificate file, we place that file in the right location (overriding the self signed certificate)

In the main playbook, we reload a last time nginx to present the new certificate to the clients.

**WARNING**: you certainly noticed the acme_directory parameter was commented. This way you use the default value which is the testing service of letsencrypt. Certificate retrieved won't be valid. It is good to test your setup works without hitting the letsencrypt service quotas (limited number of certificate requests per month for a given account). If you are sure your setup is okay and want real certificates, uncomment those 2 lines to hit the production servers.

**WARNING 2**: the agreement parameter is really important. The default value points to an outdated agreement document. LE service won't validate your certificate this way. Be sure to point to a recent version of the document.
Conclusion

I had simple needs here, configure proxy, DNS and tls for existing web applications, using infrastructure as code. Ansible is just great for that. Playbooks are really fast and easy to write (the complexity depending on the modules and roles you use) and easy to debug.

I now have to improve this setup and the roles by making PRs to upstream. I'll also merge those playbooks in an incoming ansible role. This role will be the base of configuration for the future nc42 infrastructure. This will shortly and obviously be open source.

