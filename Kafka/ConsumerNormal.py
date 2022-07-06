#!/usr/bin/env python
# coding: utf-8

# In[ ]:



# Import some necessary modules
from kafka import KafkaConsumer
from pymongo import MongoClient
from pprint import pprint
import json
from json import loads


# connect kafka consumer to desired kafka topic	
consumer = KafkaConsumer('Normal',bootstrap_servers=['localhost:9092'])


# In[ ]:


for msg in consumer:
   print(msg.value)

