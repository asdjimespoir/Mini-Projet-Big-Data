# Conception et déploiement d’un système e-health 
## Contexte
Dans les systèmes électroniques de santé ou e-health, plusieurs capteurs ou appareils IoT (Internet des objets) sont déployés pour collecter des données qui surveillent les activités, l'état et l'environnement des patients. Le but est de stocker ces données et les analyser afin de faciliter la prise de décisions automatisées pour protéger le bien-être des patients. Ces décisions peuvent avoir lieu à la périphérie du réseau pour une latence minimale (au niveau des Gateways) ou peuvent être envoyées aux systèmes Big Data côté serveur pour le stockage et les futurs diagnostics. De plus, en cas d’alertes, des notifications sont envoyées en temps réel aux aides- soignants concernés.

Dans ce mini-projet, nous décrivons plus en détails les spécifications de ce système et les composants nécessaires à son fonctionnement. Nous nous focalisons sur la conception d’une architecture Big Data permettant de respecter les spécifications et de déployer une solution tout en se basant sur les technologies sur le traitement en mode ‘batch’.
## Architecture
<img width="964" alt="Architecture" src="https://user-images.githubusercontent.com/53083052/177451032-5269919d-4908-4354-a26c-9166088feb74.png">

Dans un premier temps, nous avons choisit cette architecture afin de repondre aux exigences qu'oblige le projet.
En utilisant le cluster KAFKA, nous aspirons à une approche plus globale et en même temps performante.
Deuxièmement kafka:
* est un système de messagerie distribué open source.
* est tolérant aux pannes, performant, hautement distribuable et adapté aux traitements batchs comme streams.
* Comparé à d’autres plateformes il a la meilleure performance.
## Prérequis
* [Kafka](https://kafka.apache.org/downloads)
* [docker](https://docs.docker.com/get-docker/)
* [docker-compose](https://docs.docker.com/compose/install/)
## Mise en place de l'environ
### Démarrer les containeurs
```
docker-compose up --build -d
```
Lancer kafka
```
docker exec -it kafka bash
```
![1-Creation_des_topics](https://user-images.githubusercontent.com/53083052/177600135-ed6c2c1d-0a15-4f7e-88cd-730ebdcca9ca.gif)

### Création des topics kafka
```
kafka-topics --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 2 --topic Alerte
```

```
kafka-topics --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 2 --topic Normal
```
![1-Creation_des_topics](https://user-images.githubusercontent.com/53083052/177610386-e33b79be-b6d0-4fc4-b7a1-40afdaebfe02.gif)

### Simulation des Producteurs et Consommateurs
#### 1er Cas d'utilisation :
Nous devons utiliser le Produccer1.py afin d'envoyer des alertes aux médecins et infirmiers urgentistes tous en utilisant un fichier csv déjà prêt(avec la colonne target).
```
python Producer1.py
```
Utilisons ensuite le ConsumerAlerte.py pour lire les messages simulés d'urgence à partir du topic dédié(Alerte)
```
python ConsumerAlerte.py
```
![2-Streaming_sur_les_alertes](https://user-images.githubusercontent.com/53083052/177610943-b55ecef4-45eb-49df-b408-08899e1097d9.gif)

#### 2e Cas d’utilisation :
Dans ce cas d'utilisation, nous allons utiliser du Machine Learning afin de prédire si un patient est en état critique ou normal. Pour ce fait, nous avons un pipeline du modèle de classification choisit comme étant celui avec le meilleur score selon les tests effectués.
Le principe consiste à prédire la colonne target en supposant qu'on a un dataset n'ayant pas cette colonne. En suite une fois fait une utilisons cette colonne pour envoyer des alertes aux urgentistes (target = 0 : état normal, target = 1 : état critique).

```
python Producer2.py
```
Utilisons ensuite le ConsumerAlerte.py pour lire les messages simulés d'urgence à partir du topic dédié(Alerte)
```
python ConsumerAlerte.py
```
![6 2-Traitement_avec_prediction](https://user-images.githubusercontent.com/53083052/177611421-507d14c7-4ee3-4ade-a970-2da8a92b2093.gif)

### Sauvergarde des données sur MongoDB
Lancer Mongo
```
docker exec -it mongo bash
```
Utiliser un connecteur kafka pour récupérer des données des topics et les envoyer sur le base mongo
```
./Connector.sh
```
![Connector](https://user-images.githubusercontent.com/53083052/177611825-88f1ccd1-5ff1-457f-978b-042d6b8f6a3a.gif)

### Création des des Rôles et Utilisateurs sur la base mongo
```
mongo -u root -p root < CreateRoleAndUser.js
```
![RolesUsers](https://user-images.githubusercontent.com/53083052/177612524-3fcfc07b-9096-4d79-81dd-1d325b6a56b2.gif)

## Sources
* [Sklearn](https://scikit-learn.org/stable/)
* [Mongo Roles Users](https://www.mongodb.com/docs/manual/tutorial/manage-users-and-roles/)
* [Kafka Documentation](https://kafka.apache.org/documentation/)
* [Confluent Docker-Compose file](https://github.com/confluentinc)
* [MongoDB Connector Configuration](https://www.mongodb.com/docs/kafka-connector/current/)


## Aller plus loin
Merci de vous rendre le dossier Demo du referencciel afin de voir l'execution du projet du début à la fin.
