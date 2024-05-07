class Person:   #Class
    name = "Harry"
    occupation = "software Developer"
    networth = 10

    def info(self):     #that object in a method is call
        print(f"{self.name} is a {self.occupation}")


a = Person()  #Object

# a.name = "Shubham"
# a.occupation = "Accountant"

print(a.name , a.occupation)

a.info()