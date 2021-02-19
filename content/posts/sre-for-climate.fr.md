---
title: "La méthode SRE et le climat"
date: 2021-02-19T19:25:24+02:00
tags:
  - sre
  - automatisation
  - energie
  - scaphandre
  - open-source
  - rust
  - devops
  - résilience
  - climat
  - tech
image: /lizard.jpg
thumbnail: /lizard.jpg
share_img: /lizard.jpg
author: Benoit Petit
---

Connaissez vous les pratiques SRE (et non pas RSE) ? Ce sont des pratiques mises en avant par Google, notamment depuis la sortie du premier livre "référence" intitulé "[Site Reliability Engineering](https://sre.google/sre-book/table-of-contents/)" en 2016.   L'"ingénierie de la fiabilité des sites", en bon français (traduction brillament osée par les contributeurs de Wikipedia), a pour objectif au sein d'une organisation de s'assurer que les systèmes et services logiciels qui y sont créés sont évolutifs et surtout **très fiables**. Pour ce faire, de nombreux aspects de l'ingénierie logicielle sont appliqués aux problèmes d'infrastructure.

## DevOps, SRE, quelle différence ?

Puisque nous avons mis un pied dans le dangereux royaume des buzzwords, tentons d'y voir plus clair avant de continuer. Si vous êtes déjà familiers avec le DevOps et les pratiques SRE, vous pouvez passer directement [à la suite de cet article](#sli-slo-et-le-budget-derreur). a quelques point communs avec le mouvement DevOps, notamment :

- **Le changement est nécessaire pour s'améliorer**: adopter les méthodes DevOps ou les pratiques SRE, c'est l'inverse de l'immobilisme et des gels de déploiements sur une infrastructure. Dans les deux cas, identifier les axes d'amélioration, modifier et apprendre de ses erreurs est essentiel. Pour que cette philosophie fonctionne, il est indispensable que les incidents
- **Casser les silos** : contrairement au monde décrit dans [IT crowd](https://fr.wikipedia.org/wiki/The_IT_Crowd), les pratiques DevOps comme SRE encouragent une collaboration régulière et systématique entre les développeurs, le produit et l'infrastructure, à chaque étape d'un projet. La litterature SRE parle même de "shared ownership model" ou modèle de responsabilité partagé. Dans ce contexte, les responsables produit sont tout autant **responsables** (et donc **investis**) que les développeurs ou que les SRE, lors de la mise en place d'un changement dans un service ou une application.
- **De petits changements, fréquents** sont préferrés à de grosses mise à jour issues de plusieurs mois de développements. Ceci permet une plus grande fiabilité, en particulier si chacun d'entre eux est testé automatiquement, ce qui contribue à la [**feedback loop**](https://devops.com/faster-feedback/).
- **Un incident ou un échec n'est jamais la faute d'une seule personne** : il convient donc de comprendre l'explication systémique d'un problème (le bouton dangereux dans l'interface X n'est pas assez rouge et on ne demande pas à l'utilisateur Michel si il est sûr de lui), plutôt que de chercher un coupable (c'est la faut de Michel).

## SLI, SLO et le budget d'erreur

L'un des pilliers parmis ces pratiques sont les fameux SLI et SLO, pour Service Level Indicators and Service Level Objectives.

Un Service Level Indicator est le plus souvent un ratio entre deux nombres. L'un étant le nombre d'évennements "positifs", l'autre le nombre total d'évennements correspondants. Quelques exemples de SLI:

- nombre de requêtes HTTP soldées par un succès / nom total de requêtes HTTP sur le même service
- nombre de demandes sur mon datastore pour obtenir l'état des stocks d'un entrepot qui ont retourné un résultat en moins de 2 minutes / nombre total de demances pour avoir l'état des stocks
- nombre d'appels gRPC qui ont terminé en moins de 80ms / nombre total d'appels gRPC sur le même service

Un point important pour bien choisir un SLI est qu'il doit permettre de mesurer la satisfaction d'un client ou d'un utilisateur. C'est pour celà que l'on va plus souvent s'intéresser aux notions d'erreurs perçues par le client ou de latence, plutôt que de savoir quelle quantité de mémoire est utilisée sur le serveur, par exemple.

La deuxième notion importante ici est le Service Level **Objective**. Il s'agit ni plus ni moins que d'un objectif à atteindre sur un SLI, sur une fenêtre de temps flotante ou basée sur le calendrier (chaque mois par exmple). Cet objectif doit être défini **conjointement** entre l'équipe produit, l'équipe en charge de l'environement de production et les développeurs. Le respect de cet objectif doit également être porté ("owned") par une personne ayant suffisament de pouvoir pour faire des compromis entre la vélocité (la vitesse à laquelle les fonctionnalités sont déployées) et la fiabilité (nous y reviendrons). Ce peut donc être le CTO si c'est une petite organisation ou le product owner ou le product manager, dans une structure plus conséquente.

La différence entre 100% (de cas positifs pour le SLI) et le SLO (disons par exemple 97% de requêtes dont la réponse prend moins de 50 ms de latence) est appellée le budget d'erreur. Si le nombre de cas "négatifs" (dommageables pour la réalisation du SLO) fait tomber le SLI en dessous du SLO, on a épuisé notre budget d'erreur. Dans ce cas il faut soit revoir la conception ou l'implémentation technique du service pour respecter le SLO la prochaine fois, ou bien redéfinir le SLO si l'on se rend compte qu'il était trop ambitieux (un SLO de 100% est rarement une bonne idée).

Vous vous en doutez, le monitoring adéquat et la mise en place d'alertes lorsque le budget d'erreur est entamé ou menacé sont nécessaires. Ces indicateurs deviennent un point d'attention central des équipes de développement, de production, mais aussi de **l'équipe produit**. On pourra par exemple mettre en place un dashboard faisant état des SLI et de l'état de consommation des budgets d'erreur sur le mois, qui sera accessible de toutes les équipes concernées.

L'intérêt de cette méthode est qu'elle encourage les équipes produit, infrastructure et de développement à collaborer autour d'un **même objectif**, à savoir dans la plupart des cas, la satisfaction utilisateur.

## Qu'est ce que la fiabilité ?

Il existe plusieurs définitions de la fiabilité (notamment dans le cadre juridique). L'une d'elle a été proposée par l'[UTE](https://fr.wikipedia.org/wiki/Union_technique_de_l%27%C3%A9lectricit%C3%A9): "la fiabilité est l’aptitude d’un dispositif à accomplir une fonction requise dans des conditions données pour une période de temps donnée". Dans ce cadre on se rend compte qu'il est possible de définir les conditions qui sont données pour estimer que le dispositif (ou systême dans notre cas) a bien rempli sa mission dans la dite période.

Puisque l'IT doit baisser ses émissions de gazs à effets de serre de [45% dans les 10 prochaines années](https://www.itu.int/en/mediacentre/Pages/PR04-2020-ICT-industry-to-reduce-greenhouse-gas-emissions-by-45-percent-by-2030.aspx) si l'on veut espérer atteindre les objectifs des accords de Paris, il me semble capital qu'un système numérique ne soit considéré fiable, que si les conditions de validation de cette fiabilité inclue des objectifs concernant ses émissions de gazs à effet de serre.

Peut on dire que l'on satisfait durablement le client si l'on contribue à rendre le monde dans lequel il vivra en 2050 encore plus incertain qu'aujourd'hui ?

La méthode SRE fait de plus en plus d'adeptes et fournis un cadre de travail réellement intéressant car il encourage une collaboration entre les équipes techniques et le métier. Comme l'a très justement rappellée [Alexis Nicolas](https://www.linkedin.com/in/alexis8nicolas/) dans son [retour d'expérience]() à [Frug'agile](http://www.frugagile.org/), lutter pour amortir le changement climatique est comme un escape game dont nous faisons tous partie, qu'on le veuille ou non. C'est donc bien sûr également le cas pour chaque organisation.

Si je suis dans un escape game dans lequel l'échec signifie un réel danger pour mon entourage et ma personne (ce qui est [le cas dans celui-ci](https://meteofrance.com/actualites-et-dossiers/actualites/meteo-france-eclaire-le-climat-en-france-jusquen-2100)), je préferrerai avoir une aide dynamique pour résoudre les énigmes, des alertes automatisées si je perd trop de temps sur les mauvais éléments et une équipe qui collabore en toute transparence et qui soit pleinement concentrée sur le même objectif. Pas vous ?

## Comment aller chercher ces métriques ?

Comment avoir des métriques mesurables, comparables, mises à jour régulièrement, concernant l'impact climatique d'un service numérique ? Comment mesurer le résultat de ses efforts sur le sujet ? Il y a des sujets capitaux pour lesquels c'est compliqué (les experts de l'[ACV](https://fr.wikipedia.org/wiki/Analyse_du_cycle_de_vie) en savent quelquechose): le coût environnemental et climatique de la fabrication des machines et des terminaux, celui de la fabrication et de l'entretien des datacenters et des infrastructures, etc.

Il en est d'autres c'est possible dès à présent. La consommation d'énergie finale (ou [secondaire](https://bpetit.nce.re/fr/2021/01/scaphandre-v0.1.1-mesurer-la-consommation-d%C3%A9nergie-des-coulisses-du-num%C3%A9rique/#petites-pr%C3%A9cisions-de-rigueur)) des serveurs et des applications qu'ils hébergent en est une. [Scaphandre](https://github.com/hubblo-org/scaphandre/) est une des solutions pour y parvenir. C'est un agent de monitoring open-source, léger, dédié aux métriques de consommation d'énergie, qui s'insère simplement dans une suite de monitoring existante. Il est modulaire et simplifie les contributions  pour l'adapter à un nouveau besoin. L'idée est que c'est l'agent qui s'adapte à votre infrastructure et à vos besoins et non l'inverse. Il permet déjà de stocker les données dans [Prometheus](https://prometheus.io), [Riemann](http://riemann.io/) et bientôt dans [Warp10](https://www.warp10.io/). Ceci vous permet d'avoir toute la souplesse nécessaire par la suite pour définir vos SLI et SLO en rapport avec l'impact climatique de votre service.