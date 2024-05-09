#Creating a function
def printhello():
    print("Hello")

printhello() #Calling a function

# Creating a function with arguments
def factorial(n):
    print(n)
    fact = 1
    for i in range(n,0,-1):
        fact = fact*i
    return fact

answer = factorial(4)
print(answer)

#Function arguments
def arbitary_arguments_function(*name):  #store in a tuple
    print("Hello", name[0], name[1], name[2])

arbitary_arguments_function("Abhishek","Mohan","Sohan")

def keyword_Arbitary_arguments(**about):
    print("Hello",about["name"],about["age"],about["city"])  #store in a dictionary

keyword_Arbitary_arguments(name="Abhishek Chaudhary",age=18,city="Modinagar")