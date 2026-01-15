#Dictionaries in python
#in dictionaries we can store data in the form of key and value pair.
#we can have duplicate values but not keys.

car={
  "brand":{
    "brand1":"BMW",
    "brand2":"Benz"
  },
  "model":"nexus",
  "model2":"nexus"
}
print(car)
for i in car:
  print(car[i])
