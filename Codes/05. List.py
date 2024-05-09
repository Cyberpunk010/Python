# Creating a List of same element
Language = ["C","C++","Python","Java","Javascript"]
print(Language)

#Creating a list of Different element
About = ["Param",18,"Modinagar",True]
print(About)

#Indexing
print(Language[0])  #Poistive Indexing
print(Language[3])

print(Language[-2]) #Negative Indexing
print(Language[-4])

print(Language[2:])  #Range (start,End,JumpIndex)
print(Language[:2])

print(Language[::2]) #Unique for me

#If else in Lists
if "Modinagar" in About:
    print("City name is Present")

else:
    print("Absent")

#List Comprehension
name = ["Abhi","Dishant","Mohan","Sohan"]
new_list = [item for item in name if "o" in item]
print(new_list)