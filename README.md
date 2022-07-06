# Conception et déploiement d’un système e-health 
## Contexte
Dans les systèmes électroniques de santé ou e-health, plusieurs capteurs ou appareils IoT (Internet des objets) sont déployés pour collecter des données qui surveillent les activités, l'état et l'environnement des patients. Le but est de stocker ces données et les analyser afin de faciliter la prise de décisions automatisées pour protéger le bien-être des patients. Ces décisions peuvent avoir lieu à la périphérie du réseau pour une latence minimale (au niveau des Gateways) ou peuvent être envoyées aux systèmes Big Data côté serveur pour le stockage et les futurs diagnostics. De plus, en cas d’alertes, des notifications sont envoyées en temps réel aux aides- soignants concernés.
La figure 1 montre un exemple de système e-health déployé dans un hôpital. Des capteurs corporels sont installés au niveau du patient pour surveiller son état de santé (par exemple, fréquence cardiaque, saturation en oxygène du sang et habitudes de sommeil). D’autres capteurs de température et de pression sont installés dans sa chambre.
Dans ce mini-projet, nous décrivons plus en détails les spécifications de ce système et les composants nécessaires à son fonctionnement. Nous nous focalisons sur la conception d’une architecture Big Data permettant de respecter les spécifications et de déployer une solution tout en se basant sur les technologies étudiées dans le module Big Data I. En particulier, nous nous focalisons uniquement sur le traitement en mode ‘batch’. La partie ‘streaming’ sera étudiée l’an prochain.
## Architecture
<img width="964" alt="Architecture" src="https://user-images.githubusercontent.com/53083052/177451032-5269919d-4908-4354-a26c-9166088feb74.png">

Dans un premier temps, nous avons choisit cette architecture afin de repondre aux exigences qu'oblige le projet.
En utilisant le cluster KAFKA, nous aspirons a une approche plus globale et en meme temps performante.
Deuxièmement kafka:
* est un système de messagerie distribué open source.
* est tolérant aux pannes, performant, hautement distribuable et adapté aux traitements batchs comme streams.
* Comparé à d’autres plateformes il a la meilleure performance.
## Prérequis
* [Kafka](https://kafka.apache.org/downloads)
* [docker](https://docs.docker.com/get-docker/)
* [docker-compose](https://docs.docker.com/compose/install/)
## Mise en place de l'environ
