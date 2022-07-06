#! /bin/bash

curl -X DELETE http://localhost:8083/connectors/mongosinkUrgent_data
curl -X DELETE http://localhost:8083/connectors/mongosinkUrgent_data1

curl -X POST -H "Content-Type: application/json" --data '
  {"name": "mongosinkUrgent_data",
   "config": {
     "connector.class":"com.mongodb.kafka.connect.MongoSinkConnector",
     "tasks.max":"1",
     "topics":"Alerte",
     "connection.uri":"mongodb://root:root@mongo:27017",
     "database":"HealthDB",
     "collection":"Alerte",
     "key.converter":"org.apache.kafka.connect.storage.StringConverter",
     "key.converter.schemas.enable":false,
     "value.converter":"org.apache.kafka.connect.storage.StringConverter",
     "value.converter.schemas.enable":false
 }}' http://localhost:8083/connectors -w "\n"

 curl -X POST -H "Content-Type: application/json" --data '
  {"name": "mongosinkUrgent_data1",
   "config": {
     "connector.class":"com.mongodb.kafka.connect.MongoSinkConnector",
     "tasks.max":"1",
     "topics":"Normal",
     "connection.uri":"mongodb://root:root@mongo:27017",
     "database":"HealthDB",
     "collection":"Normal",
     "key.converter":"org.apache.kafka.connect.storage.StringConverter",
     "key.converter.schemas.enable":false,
     "value.converter":"org.apache.kafka.connect.storage.StringConverter",
     "value.converter.schemas.enable":false
 }}' http://localhost:8083/connectors -w "\n"

