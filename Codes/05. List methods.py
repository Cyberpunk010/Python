color = ["Blue","Orange","Red","Yellow"]

#Sort method
color.sort()   #Work on same instances or data type 
print(color)

color.sort(reverse=True) #In opposite order of sort
print(color)

#Reverse method
color.reverse()
print(color) 

num = [1,2,3,3,2,1,5,4,3,6,7,8]
#Index method
print(num.index(5))

#Count method
print(num.count(3))

#Copy method
copy_list = color.copy()
print(copy_list)

#Append method
copy_list.append("White")  #Take only one arguments
print(copy_list)

#Insert method
copy_list.insert(2,"Blaack")
print(copy_list)

#Extend method
color.extend(num)  #Also add other datatype
print(color) 

#Concatenating two list
print(copy_list+num)