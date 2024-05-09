#Creating a tuple
name = ("Abhishek","Mohan","Sohan")
print(name)

#Indexing
print(name[1])
print(name[-3])

#Manipulating tuple
list_name = list(name)
list_name.append("Ram")
list_name.pop(1)

name = tuple(list_name)
print(name)