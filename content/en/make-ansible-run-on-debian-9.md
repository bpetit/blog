---
title: "Make Ansible Run on Debian 9"
date: 2017-07-27T21:44:12+02:00
author: Benoit Petit
---

## How to make ansible run on debian 9 ?

Ansible version running: 2.3.1.0

Recently I upgraded personnal servers to debian stretch, as it is the new stable version. By default, the only python version installed on stretch is python3 which is not ok for ansible playbooks to execute properly. I already met that kind of issue (like everyone else) on Ubuntu above version 16.04.

Obviously the solution is to install python2.7 before running playbooks. I prefer to do that with ansible, so I have to avoid gathering_facts and run a dirty raw task on the remote host:

{{< highlight yaml "linenos=table" >}}

- hosts: all
  gather_facts: no
  tasks:
    - name: install python 2
      raw: test -e /usr/bin/python || (apt -y update && apt install -y python-minimal)

{{< /highlight>}}

This solution is ok with ubuntu 16.04 and above, but here, another error can appear on the first task you run with gather_facts: yes, like:

{{< highlight yaml >}}
Import: no module named zipfile
{{< /highlight>}}

There is certainly a difference between debian and ubuntu python2 packages which explains that zipfile module isn't shipped with python-minimal in debian stretch whereas it is in ubuntu. (I didn't dig more deeply on that topic for now)

The solution here is to install a more complete version of python2.7, the tiny playbook looks like this now:

{{< highlight yaml "linenos=table" >}}
- hosts: all
  gather_facts: no
  tasks:
    - name: install python 2
      raw: test -e /usr/bin/python || (apt -y update && apt install -y python2.7 python-minimal)
{{< /highlight>}}
