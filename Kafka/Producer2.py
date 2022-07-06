#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#importation des bibliotheques necessaires pour l'execution des lignes de codes et pipeline de la classification
import json
import joblib
from time import *
import pandas as pd
from datetime import datetime
from kafka import KafkaProducer
from xgboost import XGBClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder


# In[ ]:


producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v:json.dumps(v).encode('utf-8'))


# In[ ]:


#Appelons ce pipeline, qui inclut toutes sortes de prétraitements de données dont nous avons besoin en predisant la target variable
health_pipeline = joblib.load('/Users/Espoir/Documents/Horizon/BigData/Projet/Data/health_pipeline.pkl')


# In[ ]:


#Importation de dataset et suppression de la target variable
dfh1 = pd.read_csv("/Users/Espoir/Documents/Horizon/BigData/Projet/Data/heart.csv")
dfh1 = dfh1.drop('target', axis=1)

dfh1.to_csv('/Users/Espoir/Documents/Horizon/BigData/Projet/Data/heart_sans_target.csv', index=False)
# In[ ]:


#Importation du pipeline et predition de la target variable supprimée sur le dataset initial
dfh2 = pd.DataFrame(health_pipeline.predict(dfh1), columns=['target'])


# In[ ]:


#Concatenation des deux datasets afin d'avoir un dataset avecc la colonne target
df_test = pd.concat([dfh1,dfh2],axis = 1)
df_test.to_csv('/Users/Espoir/Documents/Horizon/BigData/Projet/Data/test.csv', index=False)
#df_test.head(34)


# In[ ]:


#Envoie des messages sur les topics en fonction de la valeur du target variable, si target =1 alors etat critique sinon etat normal
def fonctionPro(df):
    for j, row in df.iterrows():
        if (row['target'] ==1):
            if (row['sex'] ==1):
                message = {'Date':str(datetime.now()), 'Alerte!!! Patient de '+str(row['age'])+ ' ans et de sexe masculin en etat critique, infirmiere et cardiologue urgentiste requis': row.to_dict()}
                producer.send('Alerte', message)
            else:
                message = {'Date':str(datetime.now()), 'Alerte!!! Patient de '+str(row['age'])+ ' ans et de sexe feminin en etat critique, infirmiere et cardiologue urgentiste requis': row.to_dict()}
                producer.send('Alerte', message)
        else:
            message = {'Date':str(datetime.now()), 'Etat normal': row.to_dict()}
            producer.send('Normal', message)
            #sleep(1)

fonctionPro(df_test)

producer.flush()

