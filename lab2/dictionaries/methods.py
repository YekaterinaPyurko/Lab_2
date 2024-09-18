#clear()

#Remove all elements from the car list:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.clear()

print(car)

#copy() 

#Copy the car dictionary:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.copy()

print(x)

#fromkeys()
#Create a dictionary with 3 keys, all with the value 0:

x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)

#Same example as above, but without specifying the value:

x = ('key1', 'key2', 'key3')

thisdict = dict.fromkeys(x)

print(thisdict)


#get()
#Get the value of the "model" item:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")


#Try to return the value of an item that do not exist:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("price", 15000)

print(x)

#items()
#Return the dictionary's key-value pairs:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

print(x)

#When an item in the dictionary changes value, the view object also gets updated:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

car["year"] = 2018

print(x)


#keys()
#Return the keys:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()

print(x)

#When an item is added in the dictionary, the view object also gets updated:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()

car["color"] = "white"

print(x)

#pop() 
#Remove "model" from the dictionary:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.pop("model")

print(car)

#The value of the removed item is the return value of the pop() method:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.pop("model")

print(x)

#popitem()
#Remove the last item from the dictionary:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.popitem()

print(car)

#The removed item is the return value of the popitem() method:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.popitem()

print(x)


#setdefault()
#Get the value of the "model" item:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x)


#Get the value of the "color" item, if the "color" item does not exist, insert "color" with the value "white":

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "white")

print(x)


#update()
#Insert an item to the dictionary:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})

print(car)


#values()
#Return the values:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()

print(x)

#When a values is changed in the dictionary, the view object also gets updated:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()

car["year"] = 2018

print(x)
