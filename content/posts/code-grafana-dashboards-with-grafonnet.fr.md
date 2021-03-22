---
title: "Coder ses dashboards Grafana avec Grafonnet"
date: 2021-03-22T15:40:24+02:00
tags:
  - monitoring
  - grafana
  - sre
  - automatisation
  - open-source
  - devops
  - tech
image: /grafonnet.png
thumbnail: /grafonnet.png
share_img: /grafonnet.png
author: Benoit Petit
---

On ne présente plus [Grafana](https://grafana.com/) en ce qui concerne la visualisation de données de graphiques et de données. Cet outil est très largement utilisé pour des besoins de monitoring, de métrologie...

Les avantages sont multiples:

- open-source
- pratique : on peut créer des dashboards pour divers besoin très simplement
- flexible : de nombreuses sources de données sont supportées et les plugins répondent aux besoins les plus exotiques

Grafana permet également de déclencher des alertes lorsqu'une métrique dépasse une certaine valeur (plus besoin de configurer un système d'alerte propre à chaque source de donnée). C'est devenu un incontournable (en tout cas pour moi).

On peut également partager ses dashboards sous forme de fichiers JSON, ce qui est très pratique. Mais c'est là que certaines frictions peuvent apparaître : éditer du JSON à la main avec des IDs barbare et des options étranges, ce n'est pas fait pour un humain !

De plus si l'on souhaite générer des variantes de dashboards à la volée, manipuler du JSON directement, c'est un peu limité.

Si vous faîtes le même constat que moi je vous encourage vivement à regarder de plus près: [grafonnet](https://grafana.github.io/grafonnet-lib/).

Il s'agit d'une bibliothèque pour [Jsonnet](https://github.com/google/jsonnet) qui est ni plus ni moins qu'un langage de templating (ou modèle/gabarit/patron en bon français). C'est un langage qui va nous permettre de créer des modèles de dashboards, d'en faire des variantes et de les éditer **à partir du code**.

## Installation

Petite précision : je vais ici présenter [go-jsonnet](https://github.com/google/go-jsonnet), qui est une implémentation plus récente que le projet jsonnet original et réputée plus performante (je n'ai pas comparé). Si vous avez déjà joué avec des projets écrits en Go cette commande vous sera familière :

{{< highlight bash >}}
go get github.com/google/go-jsonnet/cmd/jsonnet
{{< /highlight >}}

Assurez vous alors que votre path Go est bien compris dans `$PATH` et vous pourrez lancer :

{{< highlight javascript >}}
jsonnet --help
	Jsonnet commandline interpreter (Go implementation) v0.17.0

jsonnet {<option>} <filename>
	
Available options:
  -h / --help                This message
  -e / --exec                Treat filename as code
  -J / --jpath <dir>         Specify an additional library search dir
[...]
{{< /highlight >}}

Nous allons également avoir besoin de Grafonnet, que nous allons placer dans le dossier courant :

{{< highlight javascript >}}
git clone https://github.com/grafana/grafonnet-lib.git
{{< /highlight >}}

Passons maitenant au code.

## Premier dashboard

Posons les bases de notre premier dashboard :

{{< highlight javascript >}}
local grafana = import 'grafonnet/grafana.libsonnet';
local dashboard = grafana.dashboard;
local template = grafana.template;

dashboard.new(
    'Mon super dashboard',
    tags=['super', 'dashboard'],
    editable=true
)
.addTemplate(
    template.datasource(
        'PROMETHEUS_DS',
        'prometheus',
        'Prometheus',
        hide='label',
    )
)
{{< /highlight >}}

Ici on déclare trois variables :
- `grafana` qui va comprendre le chemin vers notre bilbiothèque grafonnet (nous verrons ensuite comment appeller effectivement la bibliothèque)
- `dashboard` et `template` qui vous nous permettre de manipuler respectivement un [dashboard](https://grafana.com/docs/grafana/latest/dashboards/) et des [templates](https://grafana.com/docs/grafana/latest/variables/) sans avoir à repréciser le préfice `grafana.` à chaque fois

Puis on appelle la fonction [new](https://grafana.github.io/grafonnet-lib/api-docs/#dashboardnew) pour créer un nouveau dashboard, on lui donne un nom, des tags pour l'identifier facilement lorsque l'on aura de nombreux dashboards sur notre instance grafana et on demande à ce qu'il soit éditable (c'est toujours pratique de pouvoir tester quelques options à la main).

On appelle ensuite la fonction `addTemplate` pour créer notre variable, qui sera un [datasource](https://grafana.github.io/grafonnet-lib/api-docs/#templatedatasource) et nous permettra en un clic de séléctionner une source de donnée différente (ce qui est pratique si l'on va chercher des données dans plusieurs instances prometheus différentes par exemple).

On sauvegarde ce fichier et on le nomme `dashboard.jsonnet`.

## Utilisation

Nous allons maintenant lancer jsonnet, lui dire d'utiliser la biliothèque qui nous intéresse pour faire nos dashboards (Grafonnet) et lui donner notre template à digérer :

{{< highlight bash >}}
	jsonnet -J grafonnet-lib dashboard.jsonnet
{{< /highlight>}}

Par défaut jsonnet afficher le résultat sur la sortie standard, ce qui n'est pas très pratique. On redirige le tout dans un fichier :

{{< highlight bash >}}
	jsonnet -J grafonnet-lib dashboard.jsonnet > bidouille.json
{{</ highlight>}}

Une fois fait il n'y a plus qu'à importer le dashboard dans grafana et le tour est joué. A ce stade, on aura un dashboard vide avec notre variable en haut à gauche.

Dans mon cas, le conteneur grafana a un volume attaché qui permet de donner à grafana un répertoire de dashboards (fichiers json) par défaut, grafana [étant configuré pour charger ce dashboard](https://github.com/hubblo-org/scaphandre/blob/main/docker-compose/grafana/dashboards.yml). De cette manière je peux générer un dashboard en JSON puis redémarrer le conteneur grafana pour tester mes changements :

{{< highlight bash >}}
jsonnet -J ~/git/grafonnet-lib ../sample.jsonnet > dashboards/sample-dashboard.json && docker-compose restart grafana
{{</ highlight>}}

## Remplir le dashboard

Notre dashboard n'est pas très intéressant, c'était l'exemple de base. Voyons comment l'aggrémenter et faire un dashboard pour remonter la consommation d'énergie détaillée de mon laptop avec [Scaphandre](https://github.com/hubblo-org/scaphandre/) et la stack [docker-compose](https://github.com/hubblo-org/scaphandre/tree/main/docker-compose) qui va bien pour des tests en local.

Nous avons déjà vu les objet dashboard et template. Nous allons maintenant ajouter une ligne (row) à notre dashboard et insérer des graphes dans cette ligne. Pour ce faire, on appelle directement la fonction [addRow]() sur l'appel à la fonction [addTemplate]() vue [précédemment](#premier-dashboard):

{{< highlight javascript >}}
[...]
.addRow(
    row.new(
        title='Per hosts',
    )   
    .addPanel(
        grafana.graphPanel.new(
            title='Hosts power consumption',
            datasource='${PROMETHEUS_DS}',
            format='W',
            span=6,
        )
        .addTarget(
            grafana.prometheus.target(
                'scaph_host_power_microwatts / 1000000',
                legendFormat='{{instance}}',
            )
        )
    )
    .addPanel(
        grafana.graphPanel.new(
            title='Hosts power consumption total (dynamic time range)',
            datasource='${PROMETHEUS_DS}',
            span=4,
            bars=true,
            format='Wh',
            x_axis_mode='series',
            min=0
        )
        .addTarget(
            grafana.prometheus.target(
                'sum(avg_over_time(scaph_host_power_microwatts[1h]))/1000000',
                legendFormat='total of hosts, during displayed time window',
                interval='1h'
            )
        )
    )
)   
{{< /highlight >}}

Dans l'appel à `addRow` on créé une nouvelle ligne avec [row.new](https://grafana.github.io/grafonnet-lib/api-docs/#rownew), on donne un titre à cette ligne (ici je décide que cette ligne servira aux métriques de consommation de la machine toute entière), puis on appelle [addPanel](sur la ligne résultante).

On appelle alors [grafana.graphPanel.new](https://grafana.github.io/grafonnet-lib/api-docs/#graphpanelnew) pour créer notre graphe de consommation de la machine, en précisant l'unité (Watts), la source de données (l'instance prometheus tel que nommé avec la variable définie plus haut) et la largeur du graphique.

On ajoute ensuite une requête au graphique avec `addTarget` et un objet [prometheus.target](https://grafana.github.io/grafonnet-lib/api-docs/#prometheustarget) pour lequel on précise la requête PromQL, ici la consommation d'énergie de la machine en microwatts que l'on divise pour obtenir des watts, puis la légende.

On obtient donc :

![Dashboard grafana](/grafonnet_sample_1.png)

Comme lorsque vous éditez vos panels à la main, on peut ajouter plusieurs requêtes/courbes dans le même panel en chaînant les appels `addTarget`. De même on peut ajouter des lignes en chaînant les appels `addRow`. Ajoutons une ligne pour la consommation par socket CPU et une autre pour la consommation des processus qui tournent sur la machine :

{{< highlight javascript >}}
[...]
.addRow(
    row.new(
        title='Per CPU Sockets'
    )
    .addPanel(
        grafana.graphPanel.new(
            title='Socket power consumption',
            datasource='${PROMETHEUS_DS}',
            format='W',
            span=6,
        )
        .addTarget(
            grafana.prometheus.target(
                'scaph_socket_power_microwatts / 1000000',
                legendFormat='{{instance}} Socket {{socket_id}}',
            )
        )
    )
) 
.addRow(
    row.new(
        title='Per process',
    )
    .addPanel(
        grafana.statPanel.new(
            title='Top process consumers',
            datasource='${PROMETHEUS_DS}',
        )
        .addTarget(
            grafana.prometheus.target(
                'sort_desc(topk(3, sum by (exe) (scaph_process_power_consumption_microwatts/1000000)))',
                legendFormat='{{exe}}',
            )
        )
    )
    .addPanel(
        grafana.graphPanel.new(
            title='Filtered process (process_filter) power, by exe',
            datasource='${PROMETHEUS_DS}',
            span=8,
            format='W',
            legend_rightSide=true,
            legend_alignAsTable=true,
            legend_sideWidth='30%',
            stack=true
        )
        .addTarget(
            grafana.prometheus.target(
                'scaph_process_power_consumption_microwatts{exe=~".*${process_filter}.*"}/1000000',
                legendFormat='{{ cmdline }}',
            )
        )
    )
)
{{< / highlight >}}

J'ai également ajouté dans cet exemple une target qui fait appel à une variable `process_filter`.  La variable permet à l'utilisateur de saisir le nom du processus dont il veut surveiller la consommation d'énergie et doit donc être définie au préalable (à la suite de la première) :

{{< highlight javascript >}}
.addTemplate(
    template.datasource(
        'PROMETHEUS_DS',
        'prometheus',
        'Prometheus',
        hide='label',
    )
)
.addTemplate(
    template.text(
        name='process_filter',
    )
)
{{< / highlight >}}

Le résultat final :

![Dashboard grafana](/grafonnet_sample_2.png)

Le fichier jsonnet final se trouve [ici](https://github.com/hubblo-org/scaphandre/blob/main/docker-compose/sample.jsonnet).

