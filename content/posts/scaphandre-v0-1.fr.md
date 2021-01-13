---
title: "Scaphandre v0.1.1: mesurer la consommation d'énergie (des coulisses) du numérique"
date: 2021-01-13T15:20:24+02:00
tags:
  - numérique
  - écologie
  - énergie
  - cloud
  - scaphandre
  - open-source
image: /scaphandre.large.cleaned.png
thumbnail: /scaphandre.large.cleaned.png
share_img: /scaphandre.large.cleaned.png
author: Benoit Petit
---

![scaphandre](/scaphandre.large.cleaned.png)

## Les origines du projet

Comme d'autres petites mains de la "startup nation", j'ai été amené à travailler sur des projets à "gros volume" (tout est relatif). Je pense par exemple à des projets mettant en oeuvre des modèles de machine learning, bien souvent pour montrer la bonne publicité à la bonne personne, au bon moment. Entraîner ces modèles nécessite beaucoup de ressources (CPU, RAM, GPU, etc.). Il en va de même pour les API qui collectent des données (qui bien souvent vont permettre d'entrainer ces mêmes modèles de ML). Ces APIs, selon le nombre de *clients* qui les contactent, peuvent recevoir jusqu'à quelques milliards de requêtes par jour (voire plus, mais je n'ai pas eu l'occasion de travailler sur plus "gros").

J'ai remarqué alors que nous étions souvent très heureux du défi technique que ces systèmes représentent, mais rarement critiques du nombre de machines nécessaires.
Si l'on est un peu "éveillé" sur le fait que [l'avenir de l'humanité](https://bpetit.nce.re/fr/2020/08/pourquoi-jai-quitt%C3%A9-mon-job-qui-avait-tout-pour-plaire/#relever-la-t%C3%AAte-de-l%C3%A9cran) dépend de notre capacité à réguler et faire évoluer nos pratiques (pas qu'en informatique bien entendu), on peut se poser la question de ce qu'implique le fonctionnement de telles infrastructures et services sur le climat (et bien plus).

## Mais alors pourquoi rien n'est fait ?

J'étais moi-même incapable à cette époque de mesurer les conséquences de ces projets. Nous utilisions notamment des systèmes d'*auto-scaling* et nous étions sur un cloud public (évidemment), où la ressource est **virtuellement infinie**. Lancer de nouvelles machines, lors d'une montée en charge, ne nécessitait aucune action humaine (grâce à l'auto-scaling).
Je me suis alors rendu compte que dans un tel contexte, **la ressource IT** (CPU/RAM/GPU/...) n'a plus **aucun lien** "cognitif" avec le **monde réel**. Il est impossible en l'état de se représenter ne serait-ce qu'un ordre de grandeur de ce que le service que l'on opère consomme en terme d'énergie. Impossible alors de se rendre compte de son impact sur le climat.

Comment alors :
* rendre visible l'invisible ?  
* remettre **au centre de l'attention** des entreprises, à commencer par les gens comme moi qui y travaill([ai](https://bpetit.nce.re/fr/2020/08/pourquoi-jai-quitt%C3%A9-mon-job-qui-avait-tout-pour-plaire/))ent, **l'impact** de ces pratiques ?  
* les inciter à réduire cet impact ?  
(voire à changer de modèle mais c'est un autre débat)

## Le pouvoir des graphes

Si vous êtes habitués à voir des graphes, à recevoir des alertes, ou même à faire des astreintes, vous connaissez de ce que j'appellerai **le pouvoir des graphes**. Ce "principe" (j'ai failli écrire théorème, mais il ne faut pas pousser non plus), dont le fondement est bien réel, peut se résumer de cette manière: "tout graphique, dont l'utilisateur sait qu'il le concerne et dont la courbe évoque un comportement suspect, déclenchera une action de la part de cet utilisateur, même si il n'en comprend pas encore le sens".

En d'autres termes plus sérieux, on ne comprend ni n'agit **que sur ce que l'on mesure**.

Vous l'aurez compris, pour que la "tech" agisse sur son impact carbone, en commençant par sa consommation d'énergie ([secondaire](#petites-précisions-de-rigueur)), il faut qu'elle ait ces données sous les yeux. Il faut également qu'elle puisse s'assurer qu'une action ou une décision visant plus de sobriété a bien l'effet escompté (dommage pour ces après-midi à nettoyer les boites mails).

## Descendre sous la surface

Venons en au sujet de cet article qui est de vous présenter [scaphandre](https://github.com/hubblo-org/scaphandre), un logiciel open-source de mesure de la consommation d'énergie d'un serveur informatique ou ordinateur, mais aussi des services et applications qu'il exécute. Plus précisément, scaphandre est à la fois un outil utilisable en ligne de commande et un démon (service).

Le projet a notamment pour objectif de rendre la mesure de consommation d'énergie suffisamment simple pour que ça devienne "un basique", au même titre que le nombre de requêtes par seconde ou la latence, le temps CPU consommé ou la RAM, etc...  
  
  Scaphandre est **extensible**, il peut faire appel à différentes "logiques" pour collecter les métriques (*[sensors](https://hubblo-org.github.io/scaphandre/explanations/internal-structure.html#sensors)*) et différentes logiques pour envoyer ou exposer ces métriques (*[exporters](https://hubblo-org.github.io/scaphandre/explanations/internal-structure.html#exporters)*). Cependant, il n'exécute qu'un *sensor* et qu'un *exporter* à la fois (rien n'empêche de lancer plusieurs instances de scaphandre pour répondre à des besoins différents).
  
  Il peut donc être mis en place dans une infrastructure, **quelque soit la stack de monitoring**, puisqu'il est possible de développer un nouvel exporter pour votre [TSDB](https://blog.octo.com/introduction-aux-bases-de-donnees-temporelles/) ou outil d'analyse de données préféré, si l'*exporter* en question n'existe pas déjà. L'idée sous-jacente est que pour que ces mesures soient faites et exploitées par une majorité d'informaticiens, l'outil doit **s'adapter à l'existant** et non l'inverse.

Scaphandre est de plus développé pour être le plus léger possible, à la fois en termes de ressources et de consommation d'énergie (l'inverse serait dommageable). Sa configuration est simplissime de manière à ne pas ajouter de charge de travail supplémentaire aux personnes qui opèrent l'infrastructure.

Son usage ne s'arrête pas à l'"infrastructure". Scaphandre peut également être utilisé pour le développement, de manière à savoir, par exemple, si d'une **release** à une autre, une **application** est plus ou moins **énergivore**.

## Etat et évolution

Le projet, démarré en octobre 2020, en est à sa version 0.1.1, comprenant les fonctionnalités suivantes :

- mesure de la consommation d'énergie sur une machine physique x86, sous GNU/Linux
- mesure de la consommation d'énergie des machines virtuelles présentes sur cette même machine (fonctionne pour Qemu/KVM seulement pour le moment)
- rendre accessible à une machine virtuelle, les métriques de consommation d'énergie qui la concernent, ce qui permet au client d'un cloud privé (par exemple) de suivre son impact en installant scaphandre également sur son instance/VM
- mesure de la consommation des processus tournant sur une machine
- exposer les métriques collectées par scaphandre sous forme d'un exporter [prometheus](https://prometheus.io)
- exposer les métriques dans le terminal

Vous trouverez [ici](https://metrics.hubblo.org) un exemple de dashboard construit avec les métriques provenant de scaphandre.

Voici à quoi s'attendre dans les jours/semaines à venir :

- envoi des métriques dans [riemann](http://riemann.io/)
- mesure de la consommation d'énergie d'un cluster [kubernetes](https://kubernetes.io/) ainsi que des conteneurs et services qui tournent dessus

Et par la suite :

- estimation de la consommation d'énergie, lorsque [la mesure n'est pas possible](https://medium.com/teads-engineering/evaluating-the-carbon-footprint-of-a-software-platform-hosted-in-the-cloud-e716e14e060c) (cloud public)
- envoi des métriques dans [warp10](https://www.warp10.io/)

Le projet est écrit en [Rust](https://www.rust-lang.org/), mais il est déjà inscrit dans la [roadmap](https://github.com/hubblo-org/scaphandre/projects/1) de permettre aux contributeurs et utilisateurs de créer des "plugins" dans d'autres langages. Le possible support de MacOS est étudié ainsi que des processeurs ARM... affaire à suivre. Pour prendre connaissance du reste, ou proposer une fonctionnalité qui vous serait utile pour comprendre la consommation d'énergie d'un projet IT, c'est [ici](https://github.com/hubblo-org/scaphandre/issues) !

## Petites précisions de rigueur

* La consommation d'énergie n'est bien sûr qu'une des causes d'émissions de [GES](https://fr.wikipedia.org/wiki/Gaz_%C3%A0_effet_de_serre), parmi d'autres, d'un secteur économique. Mais les autres dépassent le cadre de cet article.

* L'électricité est une énergie secondaire, par opposition aux énergies primaires (gaz, pétrole, nucléaire, éolien, etc.) qui permettent de la produire. Pour mesurer les émissions de GES liées à la consommation d'énergie secondaire il faut connaitre les sources d'énergie primaires sollicitées (et dans quelles proportions), ce qui diffère beaucoup [d'un pays à l'autre](https://www.electricitymap.org/map). Scaphandre n'apporte donc que le premier élément pour mesurer l'impact carbone de l'utilisation ou de la conception logicielle d'un service numérique, à savoir la consommation d'énergie secondaire.