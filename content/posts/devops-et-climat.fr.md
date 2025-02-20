---
title: "Climat et numérique: pourquoi le mouvement DevOps a un rôle à jouer"
date: 2021-08-09T10:02:24+02:00
tags:
  - devops
  - climat
  - environnement
  - rse
  - sre
  - slo
  - sobriété
  - tech
image: /bird.jpg
thumbnail: /bird.jpg
share_img: /bird.jpg
author: Benoit Petit
summary: En ce moment je travaille sur une formation à l'attention des techs, côté infrastructure (avec un penchant pour les méthodes SRE/DevOps), concernant la sobriété numérique. J'en ai parlé un peu autour de moi pour savoir ce que les pros du domaine aimeraient trouver dans ce type de formation. J'ai entendu plein de bonnes idées et j'en ai gardé une bonne partie (merci à celles et ceux qui me les ont soufflé). En plus de ces idées, j'ai eu droit à des avis sur le sujet, bien entendu. Certains avis m'ont interpellé.
---
![Un oiseau](/bird.jpg)

En ce moment je travaille sur une formation à l'attention des techs, côté infrastructure (avec un penchant pour les méthodes SRE/DevOps), concernant la sobriété numérique. J'en ai parlé un peu autour de moi pour savoir ce que les pros du domaine aimeraient trouver dans ce type de formation. J'ai entendu plein de bonnes idées et j'en ai gardé une bonne partie (merci à celles et ceux qui me les ont soufflé). En plus de ces idées, j'ai eu droit à des avis sur le sujet, bien entendu. Certains avis m'ont interpellé.

Je précise que je vais un peu mélanger tous les métiers de la tech dans ce post. Le focus est plutôt sur ceux qui touchent un minimum aux infra, systèmes, réseaux, déploiements, etc. Mais j'ai le sentiment que dès que l'on parle de SRE et de DevOps, les limites sont plus floues entre les métiers, puisque plusieurs profils sont  concernés (puisque DevOps est un ensemble de pratiques et pas un métier, vous vous souvenez ?). Un développeur peut très bien être concerné par ce que j'écris, notamment si il contribue à l'automatisation chez son cloud provider préféré.

Autre précision, dans cet article, il ne faut pas confondre RSE, pour Responsabilité Sociétale des Entreprises et SRE pour Site Reliability Engineering.

## "Ceux qui gèrent l'infra n'ont pas de temps à perdre, pas de moyens et/ou pas de pouvoir"

![Les administrateurs système d'IT Crowd](/itcrowd.png)

Si l'on parle du Sysadmin unique dans une PME, à qui on demande de tout gérer sans estimer sa charge de travail, je suis d'accord. Je suis plus ou moins passé par là et je connais des gens dans cette situation. Quand on a des horaires à rallonge et que l'on enchaîne les astreintes, je comprend très bien que la sobriété ne soit pas la première chose qui nous tracasse. Les techs ne peuvent œuvrer que si le management et la direction ne leurs mettent pas des bâtons dans les roues, or une surcharge de travail, c'est bloquant pour tous les sujets.

Ceci étant dit, ce que je vois autour de moi me fait plutôt penser les choses différemment. Il suffit de regarder les salaires pratiqués pour recruter des "SRE" ou des "Ingénieurs DevOps". Outre le fait que ces intitulés de poste n'ont plus rien à voir avec les termes d'origine, on constate tout de même une chose : le marché nous est **très** favorable.

Autre exemple : Kubernetes. Pour de bonnes ou de mauvaises raisons, c'est devenu un standard dès que l'on parle d'orchestration. On peut prendre le sujet par plusieurs bouts, notamment le marketing très efficace de Google et de la [CNCF](https://cncf.io). Mais à qui parle ce marketing ? A qui sont faites les belles promesses ? Aux techs. Ce sont donc bien les tech qui se font vecteur de cette hégémonie. La plupart des tech veulent apprendre à se servir de Kubernetes, parce que c'est hype, car ça montre que l'on sait (ou du moins que l'on a envie de) gérer de grosses infrastructures, mais aussi, car ça rassure sur son potentiel d'être embauché par des entreprises intéressantes. Résultat, quand on arrive dans une boite qui a ne serait ce que de petits besoins de scalabilités ou de haute disponibilité, on dégaine k8s. Forcément, lorsqu'il faut faire grossir l'équipe, on recrute quelqu'un qui connaît la techno. La boucle est bouclée. J’admets que mon raisonnement est un peu simpliste, ça mériterai d'être creusé plus méthodiquement, mais admettez qu'il y a un fond de vrai.

La morale de tout ça, c'est que les profils techniques, notamment en lien avec DevOps ou SRE, en France, en 2021, **ont un pouvoir**. Il y a beaucoup d'offres d'emploi et moyennant de se mettre d'accord entre eux en arrivant dans une entreprise, ce qu'ils disent est accepté, car, en théorie, ils ont la connaissance.

"Et les grands groupes ?" me dira t'on. C'est vrai que dans de grandes structures les choix techniques sont souvent beaucoup plus soumis à une chaine de décision descendante. Mais j'ai au moins un exemple en tête d'entreprise importante, très, très procédurière et organisée en silo, qui a fini par adopter les technos à la mode, sous pression des techs (et certainement un peu des recruteurs/recruteuses).

## "Ca doit venir de la RSE"

![Monsieurs Propre s'occupe de tout !](/mrpropre.jpg)

Je ne l'ai pas entendu sous cette forme exacte, mais c'est ce que certaines discussions laissaient sous-entendre. Ce type d'argument me fait plaisir, car il y a un parallèle évident entre la RSE (Responsabilité Sociétale des Entreprises) et DevOps : les deux ne fonctionnent réellement que lorsque les pratiques et modes de pensées sont diffus à travers toute l'entreprise.

Il y a de nombreux d'exemples d'entreprises qui ont "mis en place le DevOps" en créant une équipe dédiée qui doit être la solution ultime à tous les problèmes. Perdu, c'est un anti-pattern.

La RSE, il me semble, suit souvent le même chemin. On créé un département RSE et on considère que le travail est fait. En pratique, ça permet d'obtenir des rapports annuels et d'enlever les touillettes en plastique à la machine à café, éventuellement de mettre en place le tri des déchets, mais ça ne va pas souvent plus loin. Comme pour DevOps, une réduction d'impact environnemental ne peut être efficace et réelle, que si tous les départements et acteurs de l'entreprise sont impliqués dans la démarche et collaborent. Ce doit être un objectif commun.

Les vrais sujets sont d'ailleurs souvent mis sur la table par les employés [eux mêmes](https://www.printemps-ecologique.fr/). Comme à l'échelle individuelle, attendre que les institutions fassent tout le travail revient à nous condamner. Il faut se rassembler pour faire bouger les logiques en place, mais aussi commencer à son échelle et sur le périmètre que l'on maitrise.

## "Notre boulot c'est la fiabilité et la valeur business"

C'est vrai. Mais depuis quand reste t'on dans les sentiers battus ? L'IT évolue considérablement, en permanence et pas uniquement sur des aspects techniques, comme ceux que l'on a évoqué dans cet article.

DevOps est un bon exemple : créer de la valeur en développant avec des cycles plus courts, mettre l'emphase sur des projets plutôt que sur des tâches et collaborer entre les équipes... Ces évolutions concernent autant le management et la gestion de projet que la partie technique. Elles ont bien sûr permis d'apporter au business, mais aussi au bien être des employés, à une meilleure compréhension du métier de chacun, etc. Bien sûr les moyens techniques ont évolué pour permettre ces évolutions, mais ce n'est pas le point de départ.

Dans un [précédent article](https://bpetit.nce.re/fr/2021/02/les-pratiques-sre-et-le-climat/), j'ai expliqué pourquoi je pense que le Site Reliability Engineering est un bon framework pour remonter les métriques de mesure d'impact sur le climat et en faire des indicateurs d'aide à la décision (sous forme de SLI/SLO). Pourquoi ne pas pousser dans cette direction ?

Cette proposition est une partie de ce qu'[Hubblo](https://hubblo.org/fr) propose. Mais je suis convaincu que ça ne doit pas être uniquement le sujet de quelques "experts" et que le monde de la tech dans son ensemble doit être un moteur de l'indispensable transition vers plus de transparence et de sobriété. Il faut pour ce faire que chaque pôle technique s'empare du sujet et se l'approprie, comme c'est le cas pour les méthodes DevOps et la modernisation des SI.

J'espère que cet article "food for thoughts" vous aura intéressé. J'aimerai que ça découle sur des discussions de fond. De même, si vous êtes arrivé à la conclusion (logique) qu'il faut agir, mais que vous ne savez pas comment ou par quoi commencer, je serai également ravi d'en parler.
