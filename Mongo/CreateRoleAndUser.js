#! /bin/bash


use HealthDB
db.createRole(
 {
  role: "roleMedecin",
  privileges: [
   {resource: {db: "HealthDB", collection: "Normal"}, actions: [ "find", "update", "insert", "remove" ] },
   {resource: {db: "HealthDB", collection: "Alerte"}, actions: [ "find", "update", "insert", "remove" ] }
  ],
  roles: [{ role: "readWrite", db: "HealthDB"}]
 }
);


db.createRole(
 {
  role: "roleInfirmier",
  privileges: [
   {resource: {db: "HealthDB", collection: "Normal"}, actions: [ "find", "update", "insert" ] },
   {resource: {db: "HealthDB", collection: "Alerte"}, actions: [ "find", "update", "insert" ] }
  ],
  roles: [{ role: "read", db: "HealthDB"}]
 }
);


db.createRole(
 {
  role: "roleChercheur",
  privileges: [
   {resource: {db: "HealthDB", collection: "Normal"}, actions: [ "find" ] },
   {resource: {db: "HealthDB", collection: "Alerte"}, actions: [ "find" ] }
  ],
  roles: [{ role: "read", db: "HealthDB"}]
 }
);

#Create user on HealthDB

db.createUser(
 {
  user: "Cardiologue",
  pwd: "pwd123",
  roles: [ { role: "roleMedecin", db: "HealthDB" } ]
 }
)

db.createUser(
 {
  user: "Pneumologue",
  pwd: "pwd123",
  roles: [ { role: "roleMedecin", db: "HealthDB" } ]
 }
)

db.createUser(
 {
  user: "Orthopediste",
  pwd: "pwd123",
  roles: [ { role: "roleMedecin", db: "HealthDB" } ]
 }
)

db.createUser(
 {
  user: "Infirmier",
  pwd: "pwd123",
  roles: [ { role: "roleInfirmier", db: "HealthDB" } ]
 }
)

db.createUser(
 {
  user: "Chercheur",
  pwd: "pwd123",
  roles: [ { role: "roleChercheur", db: "HealthDB" } ]
 }
)

