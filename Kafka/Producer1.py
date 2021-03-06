#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
from time import *
import pandas as pd
from kafka import KafkaProducer
from datetime import datetime


# In[ ]:


producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v:json.dumps(v).encode('utf-8'))


# In[ ]:


data = pd.read_csv("/Users/Espoir/Documents/Horizon/BigData/Projet/Data/heart.csv")


# In[ ]:


def foncProducer(df):
    for j, row in df.iterrows():
        if (row['sex'] ==1):
            fcm = (220 - row['age'])
            if (row['thalach'] < 60 or row['thalach'] > fcm):
                if (row['trestbps'] < 90 or row['trestbps'] > 139):
                    message = {'Date':str(datetime.now()), 'Alerte!!! Frequence cardiaque et pression arterielle anormale, cardiologue urgentiste requis': row.to_dict()}
                    producer.send('Alerte', message)
                    #sleep(5)
                else:
                    message = {'Date':str(datetime.now()), 'Alerte!!! Frequence cardiaque anormale, infirmiere urgentiste requis': row.to_dict()}
                    producer.send('Alerte', message)
                    #sleep(5)
            else:
                message = {'Date':str(datetime.now()), 'Etat normal': row.to_dict()}
                producer.send('Normal', message)
                #sleep(2)
        elif (row['sex'] ==0):
            fcm = (226 - row['age'])
            if (row['thalach'] < 60 or row['thalach'] > fcm):
                if (row['trestbps'] < 90 or row['trestbps'] > 139):
                    message = {'Date':str(datetime.now()), 'Alerte!!! Frequence cardiaque et pression arterielle anormale, cardiologue urgentiste requis': row.to_dict()}
                    producer.send('Alerte', message)
                    #sleep(5)
                else:
                    message = {'Date':str(datetime.now()), 'Alerte!!! Frequence cardiaque anormale, infirmiere urgentiste requis': row.to_dict()}
                    producer.send('Alerte', message)
                    #sleep(5)
            else:
                message = {'Date':str(datetime.now()), 'Etat normal': row.to_dict()}
                producer.send('Normal', message)
                sleep(1)


foncProducer(data)

producer.flush()


# In[ ]:


'''
cp
restecg 1 2
trestbps 90 129 139
thalach
exang 1
ca=4 inco
thal = 0

1. ??ge : ??ge en ann??es
2. sexe : sexe 
    * 1 = homme
    * 0 = femme
3. cp : type de douleur thoracique
    * Valeur 0 : angine typique
    * Valeur 1 : angine atypique
    * Valeur 2 : douleur non angineuse
    * Valeur 3 : asymptomatique
4. trestbps : pression art??rielle au repos (en mm Hg ?? l'admission ?? l'h??pital)
5. chol : cholest??rol s??rique en mg/dl
6. fbs : (glyc??mie ?? jeun > 120 mg/dl) 
    * 1 = vrai ; 
    * 0 = faux
7. restecg : r??sultats de l'??lectrocardiographie au repos
    * Valeur 0 : normal
    * Valeur 1 : pr??sentant une anomalie de l'onde ST-T (inversions de l'onde T et/ou ??l??vation ou d??pression du segment ST de > 0,05 mV).
    * Valeur 2 : hypertrophie ventriculaire gauche probable ou certaine selon les crit??res d'Estes.
8. thalach : fr??quence cardiaque maximale atteinte
9. exang : angine de poitrine induite par l'exercice. 
    * 1 = oui
    1 = oui * 0 = non
10. oldpeak : d??pression ST induite par l'exercice par rapport au repos
11. slope : la pente du segment ST de pointe ?? l'effort.
    * Valeur 0 : pente ascendante
    * Valeur 1 : plat
    * Valeur 2 : pente descendante
12. ca : nombre de vaisseaux principaux (0-3) color??s par flourosopie
13. thal : 
    * 0 = `erreur (dans l'ensemble de donn??es original, 0 correspond ?? des NaN)`.
    * 1 = d??faut fixe
    * 2 = normal 
    * 3 = d??faut r??versible 
14. cible (l'??tiquette) : 
    * 0 = pas de maladie 
    * 1 = maladie
---    
**Note sur l'??tiquette de la cible** :

`Diagnostic de la maladie cardiaque (statut de la maladie angiographique)
Valeur 0 : < 50% de r??tr??cissement du diam??tre
Valeur 1 : > 50% de r??tr??cissement du diam??tre
    
**Notes du forum de discussion de l'ensemble de donn??es** :

* Les donn??es #93, 159, 164, 165 et 252 ont `ca=4` ce qui est incorrect. Dans le jeu de donn??es original de Cleveland, ce sont des NaNs.
* Les donn??es #49 et 282 ont `thal = 0`, ??galement incorrect. Ce sont ??galement des NaNs dans l'ensemble de donn??es original.

Traduit avec www.DeepL.com/Translator (version gratuite)
'''


# In[ ]:


'''
kafka-topics --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 2 --topic Alert
kafka-topics --list --bootstrap-server localhost:9092
kafka-topics --describe --bootstrap-server localhost:9092 --topic Alerte
kafka-topics --delete --bootstrap-server localhost:9092 --topic Normal
kafka-console-consumer --bootstrap-server localhost:9092 --from-beginning --topic Vitals
kafka-console-producer --broker-list localhost:9092 --topic Alerte
'''

