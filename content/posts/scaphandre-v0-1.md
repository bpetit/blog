---
title: "Scaphandre v0.1.1: measuring the energy consumption of the tech industry (backstages)"
date: 2021-01-20T11:10:24+02:00
tags:
  - tech
  - ecology
  - energy
  - cloud
  - scaphandre
  - open-source
  - rust
image: /scaphandre.large.cleaned.png
thumbnail: /scaphandre.large.cleaned.png
share_img: /scaphandre.large.cleaned.png
author: Benoit Petit
---

![scaphandre](/scaphandre.large.cleaned.png)

## The roots of the project

As many other tech workers in startups, I've worked on pretty large scale projects (even if that's subjective). I'm talking about projects involving machine learning, for example, that are often about showing the right advertisment to the right person at the right moment. Training the machine learning models for that requires a lot of resources (CPU, RAM, GPU, etc.). The same is true with APIs that are in charge of collecting data from the clients (the data will very often be used to train the ML models). Those APIs, depending on how many clients are contacting them, will receive up to several billions requests per day (or even more, but I only speak about what I've seen).

I noticed at that time, that we were often proud and happy of the technical challenge that those systems represented, but we were very less concerned about how many machines were needed to run them.
If you are aware that [our](https://www.reuters.com/article/global-threats-biodiversity-climate-chan-idUSL8N2JO34K) [future](http://web.archive.org/web/20210113085907/https://amp.theguardian.com/environment/2021/jan/13/top-scientists-warn-of-ghastly-future-of-mass-extinction-and-climate-disruption-aoe) will depend on our ability to deeply change our usages and practices (not only in tech, obviously), you may wonder about what it means to have such energy hungry systems running for the climate (and much more).

## So, why is nothing done about it ?

I was unable myself to understand the importance of the consequences of those projects. One of the reasons was that we were using *auto-scaling* systems and we were running on public clouds (you guessed it), where tech resource is **virtually infinite**. Running new machines, to absorb a traffic surge or train a model, didn't require any human action (thanks to the auto-scaling).
I noticed then, that **tech resources** (CPU/RAM/GPU/...) **don't have any cognitive relationship** with the **real world**. It's almost impossible in that situation to visualize even a sketch of how much energy is consumed. It's even harder then to understand the consequences on the climate.

How then :
* make the invisible visible ?  
* put in sight and attention of the tech companies, starting with people like me wo are (or were) working for those companies, the **impact** of those practices ?  
* incentive them to reduce that impact ?  
(or to change their business model, but that's another story)

## The power of graphs

If you are used to graphs, to receive alarms, or even to do on-call shifts, you know what I'll call **the power of graphs**. This principle (I've almost written "theorem" but that would be a bit exagerated), whose base is very real, can be summarized like this: "if a user knows (s)he is concerned with a graph, will do something about it, even if (s)he doesn't know yet what it means".

In other more serious words, we only act on what we **measure**.

To have the tech industry reflect and act on its own climate impact, starting with its ([secondary](#petites-précisions-de-rigueur)) energy consumption , it needs to see its impact and understand it. It's also very important that the efficacity of decisions and actions targeting tech sufficiency can me measured.

## Going under the surface

Let's go the to core of this article which is to present you [scaphandre](https://github.com/hubblo-org/scaphandre), an open-source software to **measure power consumption on a server** or a personnal computer. It can also measure the power consumption of a **single process or application** on the host. To be more precise, scaphandre is a CLI tool and system service (daemon).

This project intends to be simple enough to setup and use, so that power consumption metrics become basic stuff, like the number of requests per second, the latency, the CPU usage, etc. There shall be **no more excuses** to not measure and understand the power consumption of a tech service or system.  
  
  Scaphandre is **extensible**, as he can collect the metrics in different ways (*[sensors](https://hubblo-org.github.io/scaphandre/explanations/internal-structure.html#sensors)*) and send or expose those metrics in different ways (*[exporters](https://hubblo-org.github.io/scaphandre/explanations/internal-structure.html#exporters)*). However, it only executes one *sensor* and one *exporter* at a time (it's okay to run several instance of scaphandre on the same host for different needs).
  
  Because of that, scaphandre can be setup in an infrastructure, **whatever the monitoring stack is**, as you can develop a new exporter for your favorite [TSDB](https://en.wikipedia.org/wiki/Time_series_database) or data analysis tool, if the needed exporter doesn't exist already. The idea behind that is that for many tech companies and workers to use it, **the tool must adapt to what's in place** and not the opposite.

Scaphandre aims to be as light as possible, both in terms of ressources and of energy consumption (the opposite would be sad). Its configuration is very simple to not add extra work to the people using it.

Its usage doesn't stop at the infrastructure level, as it can be used to track the power consumption of an application, from one **release** to the other, to see if things are getting better, or worse.

## State and evolution

The project is under the Apache-2.0 license and started in octobre 2020. The 0.1.1 version has been released. It contains the following features so far :

- measuring the energy consumption of an x86 based **bare metal** machine, with GNU/Linux running
- measuring the power consumption of the **virtual machines** running on the host (working for Qemu/KVM so far)
- expose to a virtual machine, its energy consumption metrics, to allow a **private cloud user** to track and understand his own impact, and use those metrics directly from the instance/VM as it was available in the first place
- measuring the energy consumption of the **processes** running on a host
- expose the metrics as a [prometheus](https://prometheus.io) exporter
- display the metrics in the terminal

[Here](https://metrics.hubblo.org) is a sample dashboard where you can see some metrics that scaphandre is able to provide.

Some features should come in the following days or weeks :

- sending metrics to [riemann](http://riemann.io/)
- measuring the energy consumption of a [kubernetes](https://kubernetes.io/) cluster, and the pods and application running on it

And a bit later :

- estimating the energy consumption when [measuring is not an option](https://medium.com/teads-engineering/evaluating-the-carbon-footprint-of-a-software-platform-hosted-in-the-cloud-e716e14e060c) (public cloud)
- sending the metric to [warp10](https://www.warp10.io/)

Scaphandre is written in [Rust](https://www.rust-lang.org/), but we have added to the [roadmap](https://github.com/hubblo-org/scaphandre/projects/1) to allow contributors to write plugins in other languages. Being able to measure on MacOS and on ARM CPUs is also being studied... stay tuned. To read about the other items of the roadmap, or speak about a feature that may help you track and shrink the energy consumption of a tech project, [please reach us](https://github.com/hubblo-org/scaphandre) !

## Some precisions

* The energy consumption is only one of the vectors of greenhouse gazes emissions of an industry, among others, of course. The others are beyond the scope of this article.

* Electricity is a **secondary** energy, different from the primary energies (gaz, oil, nuclear, wind, etc.) which are used to produce it. To measure the greenhouse gazes emissions resulting from consuming electricity, you need to know the primary energies used (and how much, for each of them), which is very different [from one country to another](https://www.electricitymap.org/map). Scaphandre only gives the first item needed to get the climate impact of the design or the usage of a tech service, which is the secondary energy consumption.