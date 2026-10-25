---
title: "Revue de la littérature récente concernant les ilots de chaleur attribués aux data centers"
date: 2026-09-07T15:20:24+02:00
toc: true
tags:
  - numérique
  - écologie
  - énergie
  - datacenter
  - chaleur
image:
thumbnail: 
share_img: 
author: Benoit Petit
summary: .
---

# Revue de la littérature récente concernant les îlots de chaleur attribués aux data centers

## Introduction

Le sujet de la production d'îlots de chaleur par les data centers a émergé récemment dans le débat public, notamment suite à la sortie d'une étude menée par Andrea Marinoni et son équipe de l'Université de Cambridge [^1]. Elle a notamment été relayée par Valérie Masson-Delmotte [^2], mais également par la presse [^3] [^4].

Cette étude avance des écarts de température de 2 °C en moyenne, et pouvant atteindre 9 °C, aux abords de grands data centers d'IA. Un tel écart de température génère naturellement de l'inquiétude, surtout au sortir de la canicule historique que nous avons vécu cet été, et alors que les projets d'implantation de nouvelles installations se multiplient, parfois à proximité immédiate de zones résidentielles.

Il se trouve que cette étude a également été vivement critiquée par certains spécialistes [^7]. Si la critique brute ne fait qu'envenimer le débat, elle peut aussi être le point de départ d'une meilleure compréhension des enjeux autour de ce sujet. J'ai par ailleurs reçu plusieurs demandes concernant mon avis sur cette question, sur laquelle je n'avais jamais eu l'occasion de travailler jusqu'à présent. J'ai donc commencé par rassembler les études qui me semblaient pertinentes concernant le dégagement de chaleur, le phénomène d'îlot de chaleur et plus largement les interactions thermiques entre les data centers et leur environnement.

Cet article propose un état des lieux rapide — et probablement incomplet — des études que j'ai pu consulter à ce jour sur le sujet. Les trois premiers chapitres résument les études rencontrées. Le quatrième propose une synthèse des enseignements cumulés de ces trois études, appuyée sur un tableau récapitulatif.

Vous trouverez les sources et mes conclusions à ce stade en fin d'article.

## The data heat island effect: quantifying the impact of AI data centers in a warming world

La première étude, publiée en 2026 par Marinoni et al. [^1], s'est attachée à quantifier l'impact des data centers d'IA sur la température de surface. Il s'agit d'un **preprint**, donc d'un travail qui n'a pas encore passé le filtre de la revue par les pairs.

### Méthodologie

L'approche repose sur le croisement de données de relevés de température en surface, avec la localisation de grands data centers d'IA, sur un vaste jeu de données. Les objectifs affichés sont :

- quantifier l'augmentation de la température de surface du sol (land surface temperature) liée à l'implantation d'un datacenter spécialisé pour l'IA Générative
- évaluer la zone concernée de cette augmentation
- estimer la population affectée par cette hausse des températures.

### Résultats

L'étude conclut à une augmentation moyenne de 2 °C, avec des maxima atteignant 9 °C. L'effet s'étendrait jusqu'à 10 km autour des sites, avec une intensité décroissante (jusqu'à 30 % de l'effet subsistant à 7 km).

### Limites

Plusieurs limites méthodologiques importantes doivent être signalées :

- l'étude ne vérifie pas si l'écart observé provient de l'artificialisation des sols (bitumage, suppression de végétation, modification de l'albédo) ou réellement de la chaleur émise par les serveurs et les systèmes de refroidissement
- elle ne sépare pas l'effet du au centre de données de la tendance générale au réchauffement (baseline trend)
- la résolution satellitaire utilisée est trop grossière pour distinguer précisément le site lui-même de son environnement immédiat.

Enfin, le contexte d'étude porte sur des zones peu denses, éloignées des villes, ce qui limite la transposition des résultats aux zones urbaines.

## Data Center Waste Heat as an Emerging Urban Thermal Hazard: First Field Measurements of Neighborhood-Scale Air Temperature Impacts

La deuxième étude, publiée en 2026 par Sailor, Abolhassani et Martin [^5], est une **communication** parue dans ASME : il s'agit donc d'un travail **revu par les pairs**, mais d'un format court, à considérer comme des premières mesures de terrain plutôt que comme une démonstration définitive.

### Méthodologie

Contrairement à la première, cette étude repose sur des **mesures réelles** de la température de l'air, réalisées par traversées en véhicule autour du data center, dans des quartiers résidentiels, croisées avec des données météorologiques (notamment la vitesse et la direction du vent).

### Résultats

Les auteurs observent des écarts **maximaux de 2 °C**, mais des **moyennes** nettement **plus modestes**, **entre 0,7 et 0,9 °C**. L'effet est ressenti jusqu'à **environ 500 m autour** des installations. L'étude porte sur des data centers de 36 MW à 160 MW, situés dans des **zones urbaines denses**.

### Limites

- les mesures en zone urbaine ne permettent pas une couverture complète du rayon d'influence (les mesures sont contraintes au réseau routier)
- le périmètre d'étude (quatre data centers) reste limité.

C'est toutefois **la seule des trois études qui repose sur des mesures directes** de la température de l'air, en tenant compte des schémas de vent, ce qui en fait un point de comparaison précieux.

## L'investigation d'Amezana Roboto

La troisième étude est une **investigation** publiée en 2026 par Amezana Roboto[^6], également non soumise à la revue par les pairs.

### Méthodologie

Comme celle de Marinoni et al., elle repose sur des données satellitaires et météorologiques, mais avec une résolution **33 fois supérieure**. Elle porte sur **un seul data center de 11 MW**, en **zone urbaine**, et s'appuie sur un jeu de données de 32 000 points de température.

### Résultats

L'apport principal de cette investigation est la **séparation des causes** : les auteurs distinguent l'effet de l'artificialisation des sols de l'effet propre du refroidissement et des serveurs. Sur un écart total de 2 °C (artificialisation et tendance de fond comprises), seuls environ **17 % seraient attribuables au refroidissement**, soit **environ 0,3 °C**. Le rayon d'influence retenu est de **150 m**, avec une décroissance au-delà.

### Limites

- il ne s'agit pas de mesures directes, contrairement à l'étude de Sailor et al.
- la question centrale est celle de la modélisation utilisée pour séparer l'effet de l'artificialisation de celui du refroidissement : quelle que soit la finesse de la résolution, cette séparation repose sur un modèle, dont il faut évaluer la robustesse avant d'adopter ses conclusions

## Qu'en retenir ? Comparaison des trois études

Voici tableau récapitulatif des différences entre ces études, leurs résultats et leurs méthodologies. Vous pouvez directement consulter ce tableau, pour une vue d'ensemble rapide.

|                        | The Data Heat Island Effect: Quantifying the Impact of AI Data Centers in a Warming World      | Data Center Waste Heat as an Emerging Urban Thermal Hazard: First Field Measurements of Neighborhood-Scale Air Temperature Impacts | Amezana Roboto’s investigation                                                                                                                                                                          |
| ---------------------- | ---------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Authors                | Marinoni et al.                                                                                | Sailor et al.                                                                                                                      | Amezana Roboto                                                                                                                                                                                          |
| Year                   | 2026                                                                                           | 2026                                                                                                                               | 2026                                                                                                                                                                                                    |
| Peer reviewed          | No (preprint)                                                                                  | Yes, published in ASME                                                                                                             | No (investigation)                                                                                                                                                                                      |
| Methodology            | Satellite and meteorological hitoric data, AI data centers locations                           | Vehicle based actual measurements around the data centers, crossed with meteorological data (wind)                                 | Satellite and metorological data                                                                                                                                                                        |
| Radius                 | Up to 10km, intensity decreasing, down to 30% at 7km                                           | Up to 500m                                                                                                                         | 150m, then 300m with a decrease                                                                                                                                                                         |
| Temperature difference | 2C average, up to 9C maximum difference recorded                                               | 0.7 - 0.9C average, up to 2C in only one scenario                                                                                  | 0.3 C attributible to servers and cooling, 2C difference total combined with artificialization, baseline trend                                                                                          |
| Kind of Datacenters    | AI Data centers (big dataset)                                                                  | 36MW to 160 MW (4 datacenters)                                                                                                     | 11 MW (only one datacenter)                                                                                                                                                                             |
| Weaknesses             | \- doesn’t differentiate baseline trend, artificialization effect, from servers/cooling effect | \- urban area measurements not allowing for a complete radius coverage                                                             | \- not actual measurements - how about the modelization for separating artificialization from cooling system ?                                                                                          |
| Strength               | \- area covered                                                                                | \- actual measurements, accounting for wind pattern and velocity                                                                   | \- Satellite data resolution (30x higher than Marioni’s) - Separates artificialization effect, baseline trend, from actual servers/cooling effect - size of the dataset : 32000 temperature data points |
| Context                | Lesser dense areas, far from cities                                                            | Dense urban areas                                                                                                                  | Urban area                                                                                                                                                                                              |

Ce tableau fait ressortir trois points essentiels. Premièrement, les ordres de grandeur divergent fortement : 2 °C en moyenne pour Marinoni et al., moins de 1 °C pour Sailor et al., et environ 0,3 °C attribuables aux serveurs et au refroidissement selon Amezana Roboto.

Deuxièmement, les contextes ne sont pas comparables : zones peu denses pour la première, zones urbaines denses pour les deux autres, ce qui peut expliquer en partie les écarts de rayon d'influence observés (jusqu'à 10 km contre 150 à 500 m).

Troisièmement, seule l'étude de Sailor et al. repose sur des mesures de terrain ; les deux autres s'appuient sur des données satellitaires, avec des résolutions très différentes.

Enfin, l'investigation d'Amezana Roboto soulève un point essentiel: quelle est la part du réchauffement observé qui est effectivement attribuable au centre de données et comment estimer cette part correctement ? Cette question semble cruciale pour les futures recherches sur le sujet, en vue de permettre de répondre à cette quesion plus largement tout en restant juste d'un point de vue scientifique.

## Conclusion : des données encore insuffisantes, une lecture à manier avec prudence

Au terme de cette revue, le constat est clair : **il manque aujourd'hui des données fiables et des études évaluées par les pairs** pour trancher la question de l'ampleur réelle des îlots de chaleur attribuables aux data centers. Sur les trois travaux examinés, un seul a été soumis à la revue par les pairs, et il s'agit d'une communication courte portant sur quatre sites.

Les deux autres sont un preprint et une investigation, dont les résultats les plus médiatisés (2 °C en moyenne, jusqu'à 9 °C) correspondent précisément à l'étude dont la méthodologie est la plus contestée.

Face à cette situation, plusieurs invitations à la prudence s'imposent :

- **Ne pas confondre les causes.** Un écart de température mesuré autour d'un data center peut provenir de l'artificialisation des sols (bitume, suppression de végétation, albédo modifié), de la tendance générale au réchauffement, ou de la chaleur réellement rejetée par les serveurs et les systèmes de refroidissement. Ces trois causes doivent être identifiées et quantifiées séparément avant toute conclusion, et c'est précisément ce que j'espère voir dans les futures études sur le sujet.

- **Interroger les modèles.** Lorsqu'une étude affirme séparer l'effet de l'artificialisation de celui du refroidissement, cette séparation repose nécessairement sur un modèle. La qualité des conclusions dépend donc directement de la qualité, de la transparence et de la validation de ce modèle — un point trop souvent absent des résumés et des articles de presse qui relayent les résultats.

- **Attendre la revue par les pairs avant d'extrapoler.** Les résultats actuellement disponibles sont préliminaires, parfois contradictoires, et obtenus dans des contextes (zone urbaine dense ou non, taille du site, climat local) qui ne se transposent pas d'un site à l'autre.

En l'état, rien ne justifie ni l'alarmisme ni le déni : la question est légitime et mérite d'être étudiée rigoureusement, mais les réponses définitives restent à venir. La prudence méthodologique — sur la classification des causes d'émission de chaleur, sur la robustesse des modèles utilisés, et sur le statut de publication des études — est la seule posture tenable en attendant que la littérature scientifique s'étoffe et converge.

Ceci étant dit, il ne faut pas oublier de préciser que le secteur va bien plus vite que la recherche sur ce sujet, alors que les effets du déreglement climatique s'accélèrent, notamment concernant les températures en ville. Les manques actuels en terme de recherche ne doivent pas permettre de classer la problématique comme un faux problème.

## Sources

[^1]: Marinoni A. et al. (2026), *The data heat island effect: quantifying the impact of AI data centers in a warming world*, preprint arXiv, Université de Cambridge — [https://arxiv.org/abs/2603.20897](https://arxiv.org/abs/2603.20897)

[^2]: Masson-Delmotte V., *Les enjeux environnementaux des data centers* (note de synthèse relayant notamment l'étude de Cambridge), juin 2026 — https://www.elan-savigny-environnement.org/2026/06/04/les-enjeux-environnementaux-des-data-centers/

[^3]: *AI datacenters create heat islands around them, paper finds*, The Register, 1er avril 2026 — https://www.theregister.com/2026/04/01/ai_datacenter_heat_islands/

[^4]: *Data centers create 'heat islands,' warming local land by up to 16.4°F (9.1°C)*, The Independent — https://www.independent.co.uk/climate-change/ai-data-center-heat-islands-usage-climate-b2949418.html

[^5]: Sailor D. J., Samareh Abolhassani S., Martin E. P. (2026), *Data Center Waste Heat as an Emerging Urban Thermal Hazard: First Field Measurements of Neighborhood-Scale Air Temperature Impacts*, Journal of Engineering for Sustainable Buildings and Cities, ASME, 7(2) — https://doi.org/10.1115/1.4071922

[^6]: Amenaza Roboto (2026), *The Heat Behind the Cloud* (investigation sur le data center Antel de Pando, Uruguay) — https://amenazaroboto.com/the-heat-behind-the-cloud

[^7]: Masley A., *Data centers' heat exhaust is not raising the land temperature of nearby areas* (critique de l'étude de Cambridge) — https://blog.andymasley.com/p/data-centers-heat-exhaust-is-not

[^8]: Fortune, *Data centers are so hot their 'heat island' effect is raising surrounding temperatures*, 1er avril 2026 — https://fortune.com/2026/04/01/ai-data-centers-heat-island-hyperscalers/
