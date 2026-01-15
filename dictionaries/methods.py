#Methods in dictionaries
car={
  "brand":"TATA",
  "model":"RR",
  "price":2000,
  "colour":{
    "colour1":"red",
    "colour2":"white"
  }
}

# for key, value in car.items():
#   if isinstance(value, dict):
#     for key1, value2 in value.items():
#       print(key1, value2)
#   else:
#     print(key, value)

for key, value in car["colour"].items():
  print(key, value)



# #keys()
# print(car.keys())

# #values()
# print(car.values())

# #items()
# print(car.items())

# #update()
# car.update({"brand":"Tesla"})
# print(car)

# #pop()
# removed=car.pop("brand")
# print(removed)
# print(car)

# #popitem()
# car.popitem()
# print(car)

# #copy()
# car2=car
# print(car2)


