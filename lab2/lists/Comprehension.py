fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


#newlist = [expression for item in iterable if condition == True]

newlist = [x for x in fruits if x != "apple"]


#With no if statement
newlist = [x for x in fruits]


#range()
newlist = [x for x in range(10)]

#Accept only numbers lower than 5
newlist = [x for x in range(10) if x < 5]

#Expression

newlist = [x.upper() for x in fruits]

newlist = ['hello' for x in fruits]

newlist = ['hello' for x in fruits]



