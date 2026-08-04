---
title: "Why the '100% electricity coming from renewables' claims from Cloud, AI and Datacenters providers are not okay, and what could be done instead"
date: 2026-08-04T16:59:24+02:00
toc: true
tags:
  - ghg
  - climate
  - ghgprotocol
  - datacenters
  - scope2
  - emissions
  - electricity
  - rec
  - ppa
  - goo
  - market
image: /solar_panels.webp
thumbnail: /solar_panels.webp
share_img: /solar_panels.webp
author: Benoit Petit
---

*Image: solar panels reflecting the sun, from [Alex Lang](https://www.flickr.com/photos/40888529@N00/3546825820)*

We get transparency only as good as regulation makes it. Even knowing that, I'm still puzzled every time I see a "100% renewable energy" label regarding the electricity consumption of any service provider.

It's not just in the Datacenter industry. Every single provider of service, including the ones that otherwise really tries to be a bit more sustainable than the average, intentionally (how handy) or unintentionally fall into this trap (sometimes using the claims of their own providers).

I'm used to discuss about this with people who are well aware, but I feel as this type of claims are still everywhere, that I am one of those people not contributing enough to explain it to a wider audience to contribute to stop this practice.  

To put it simple:
- yes having as much renewables as possible in the electricity you consume for a service is a good thing (but you cant just buy something to make this happen for real)
- no it is currently, absolutely, **not** possible to achieve 100%  

Why ? There is simply no electricity grid on earth that achieved that goal, detailling why is another topic. There is neither any provider, except very few exceptions that are not representative of the services consumed on a day to day basis, that achieved that goal for their own consumption with local renewable based production.

Every provider that says otherwise is relying on guarantees of origin certificates to justify the origin of its electricity.

What are Guarantees Of Origins certificates ? You'll find them under different names with nuances of implementation (RECs, PPAs, GoOs, ...) but what you need to have in mind is the base principle:

- the provider of the service buys a certificate for 1 MWh of electricity to a producer, depending on the type of certificate this will either account for a current project actually producing electricity with renewables OR a future project/power plant that remains to be constructed
- if this is a running power plant, it will retribute the producer for electricity already produced, but sometimes also secure some of the future production by financing it at a fixed price (PPAs can do that, see below)
- if this is a future project, the idea is that buying this certificate contributes to finance the new power plant, thus enabling more renewables available on the grid later, which is a good thing, but details matter (see below)

There are mainly 3 issues why such labels are extremely problematic:

## It is simply not true and misleading for the consumer

The most obvious one, and the main reason why I think labeling  "100% electricity produced from renewables" should be forbidden (except if the provder effectively covers 100% of his absolute value consumption with local renewables), is that this sends the wrong message:

- has it reduced the footprint of the electricity consumption ?  

**NO**, the very same electricity as anyone connected to the grid as been consumed. But reminder: this is how companies are artificially/accountingly lowering "scope 2" emissions figures from their activity (if the data are "market-based" and not "location-based")

- has it contributed to make the renewables production market stronger ?

Y.. **MAYBE** (why not yes, below)

On paper, saying "we covered 100% of our electricity consumption with equivalent financial investment in renewables production" or something approaching would be completely fine, as long as you don't make magically disappear the GHG emissions of your electricity consumption in your environmental display thanks to those certificates (this is what you get as "market-based" carbon footprint data, look for location based instead). It would display that the provider supports having more renewables globally, while not pretending that the electricity actually consumed comes from something else than the fossil fuel + renewables (+ sometimes nuclear) mix.

But this is not that simple, as there is a lot of uncertainty about the real effect of the certificate on the actual renewable production.
  
## Double counting happens

Meaning having two companies [buying the same MWh of electricity](https://industrydecarbonization.com/news/how-iceland-sold-the-same-green-electricity-twice.html) from the same renewables-based producer. To understand how and when this happens requires to read a bit more about the different types of certificates and what they imply. The problem with GoOs and RECs (the most permissive types of certificates) is described [here](https://industrydecarbonization.com/news/the-trouble-with-european-green-electricity-certificates.html) and [here](https://industrydecarbonization.com/news/double-counting-and-other-problems-with-green-electricity-certificates.html).    
  
## Guarantee of Origins certificates, in their "unbundled" version may be emitted for existing production capacities

For example an old hydro power plants there for decades, so there is no way the certificate is involved in helping top build new capacity, plus there are other accountability issues that can rigg the game (see sources below for details).
  
PPAs are reputed to be a better type of certificate, as they imply conditions that make the act of buying the certificate more likely to be linked to an actual effect for an electicity producer, at least reserving future production at fixed price so the producer survives an electricity price drop, securing the project on a longer term. However, the details matter, this more concrete connection between consumer and producer is not ensured in the same way whether this is an on-site, a sleeved, or virtual PPA. Vitual PPAs being the worst case as the producer can be connected to totally different electricity grid than the consumer.

As this is already a too long post, I'll finnish with resources to dig deeper, with [this very large bibliography on the topic made by the University of Edinburgh](https://www.bccas.business-school.ed.ac.uk/research/carbon-accounting-pricing-policy/renewable-energy-purchasing), or for french readers, I've contributed to describe this in the [Ademe's 2024-2060 prospective study on Datacenters consumptions, pages 47-48](https://librairie.ademe.fr/energies/8910-prospective-d-evolution-des-consommations-des-data-centers-a-court-moyen-et-long-terme-de-2024-a-2060.html).

To conclude, I think having a label that shows the financial investment of a provider in renewables would be a good thing, as companies are not people and often need to be rewarded in someway to actually do something. However, it should be differenciated from the claim of having renewables in the electricity mix consumed, which depends from the long term investments policy from companies and states, and the political direction regarding greening the grid. Once again in the quest of sustainability, politics 1 - 0 market.

PPAs, excluding virtual PPAs, could be a good thing to help building new renewables (especially regarding the latest developments on time based PPAs, closer to what happens in reality), but the labelling on top of their usage matters and should be reglemented firmly.

Finally, those claims are the root of some of the [most rigged figures](https://www.theguardian.com/technology/2024/sep/15/data-center-gas-emissions-tech) about BigTech's scope 2 / electriciy consumption GHG emissions you can see. Avoid market based data at all cost and challenge labels, always.
