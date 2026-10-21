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

Le sujet de la production d'ilot de chaleur par les data centers a émergé récemment, notamment suite à la sortie d'une étude de l'Université de Cambridge[^1], relayée notamment par Valérie Masson Delmotte[^2], mais aussi par la presse [^3] [^4].

Cette étude avance des écarts de température en moyenne de 2C et jusqu'à 9C aux abords de grands data centers d'IA, aux... . Un tel écart de température génère naturellement de l'inquiétude, surtout au sortir de la canicule historique que nous avons vécu cet été. 

Il se trouve que cette étude a été également vivement critiquée par X, Y et Z. Si la critique brute ne fait qu'envenimer le débat, elle peut être le point de départ d'une meilleure compréhension des enjeux autour de ce sujet.
J'ai également reçu plusieurs demandes concernant mon avis sur ce sujet, sur lequel je n'avais jamais eu l'occasion de travailler jusqu'à présent. J'ai donc commencé comme d'habitude, par rassembler les études qui semblent pertinentes concernant le dégagement de chaleur, le phénomène d'ilot de chaleur, ou bien le 

Cet article propose un état de lieux rapide (probablement incomplet) des études que j'ai pu consulter à ce jour sur le sujet. Les trois premiers chapitres résument les études rencontrées. Le quatrième est une synthèse des enseignements cumulés de ces trois études. 

### The Data Heat Island Effect: Quantifying the Impact of AI Data Centers in a Warming World

Cette étude, de Marinoni et al

** outside of cities **

**preprint**

method:
- satellite data crossed with data center locations

2026

• Quantification of the land surface temperature increase connected to the establishment of an AI  hyperscalers;
• Assessment of the region of influence of this increase;
• Estimation of the population affected by the temperature increase.

2C average **but** (up to 9C max):
- doesn't check if because of artificialization or really from the heat coming from servers and cooling system
- doesn't separate from the general trend
- too large resolution to be precise and distinguish from the local area

### Data Center Waste Heat as an Emerging Urban Thermal Hazard: First Field Measurements of Neighborhood-Scale Air Temperature Impacts

Sailor D
Abolhassani S
Martin E

**communication**

2026

method:

- vehicle based traverse measurements of air temperature in residential neighborhoods

** in dense cities **

2c max, average of 0.7 - 0.9

up to 500m

### Amezana Roboto

2026

33 times higher resolution than marioni's

separates artificialization effect from the actual cooling effect

2c difference but : 17% only from cooling ~= 0.3 C

150m radius, different from other kind of facilities
300m with a decrease  

## Qu'en retenir ?

En fin d'article se trouve un tableau récapitulatif des différences entre ces études, leurs résultats et leurs méthodologies. Vous pouvez directement consulter ce tableau, pour une vue d'ensemble rapide.

## Revue de littérature concernant les ilots de chaleur attribuables aux data centers

|                        | [The Data Heat Island Effect: Quantifying the Impact of AI Data Centers in a Warming World]() | [Data Center Waste Heat as an Emerging Urban Thermal Hazard: First Field Measurements of Neighborhood-Scale Air Temperature Impacts]() | [Amezana Roboto's investigation]()                                                                                                                                                                         |
|------------------------|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Authors                | Marinoni et al.                                                                               | Sailor et al.                                                                                                                      | Amezana Roboto                                                                                                                                                                                         |
| Year                   | 2026                                                                                          | 2026                                                                                                                               | 2026                                                                                                                                                                                                   |
| Peer reviewed          | No (preprint)                                                                                 | Yes, published in ASME                                                                                                             | No (investigation)                                                                                                                                                                                     |
| Methodology            | Satellite and meteorological hitoric data, AI data centers locations                          | Vehicle based actual measurements around the data centers, crossed with meteorological data (wind)                                 | Satellite and metorological data                                                                                                                                                                       |
| Radius                 | Up to 10km, intensity decreasing, down to 30% at 7km                                          | Up to 500m                                                                                                                         | 150m, then 300m with a decrease                                                                                                                                                                        |
| Temperature difference | 2C average, up to 9C maximum difference recorded                                              | 0.7 - 0.9C average, up to 2C in only one scenario                                                                                  | 0.3 C attributible to servers and cooling, 2C difference total combined with artificialization, baseline trend                                                                                         |
| Kind of Datacenters    | AI Data centers (big dataset)                                                                 | 36MW to 160 MW (4 datacenters)                                                                                                     | 11 MW (only one datacenter)                                                                                                                                                                            |
| Weaknesses             | - doesn't differentiate baseline trend, artificialization effect, from servers/cooling effect | - urban area measurements not allowing for a complete radius coverage                                                              | - not actual measurements - how about the modelization for separating artificialization from cooling system ?                                                                                          |
| Strength               | - area covered                                                                                | - actual measurements, accounting for wind pattern and velocity                                                                    | - Satellite data resolution (30x higher than Marioni's) - Separates artificialization effect, baseline trend, from actual servers/cooling effect - size of the dataset : 32000 temperature data points |
| Context                | Lesser dense areas, far from cities                                                           | Dense urban areas                                                                                                                  | Urban area                                                                                                                                                                                             |

## Definitions

Thermal plume

Hot-air reject from the data center into the environment, whose neighbourhood impact must be assessed.

Heat island

Local overheating from rejects and built form, near the site.

Dispersion

Dilution of the hot plume by the wind, which conditions its impact on the ground and neighbours.

[]: [Offre du cabinet eolios pour l'analyse](https://eolios.eu/data-center/urban-heat-island-impact-study-for-data-centers/)