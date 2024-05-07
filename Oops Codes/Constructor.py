class Person:

    def __init__(self,name,occ):
        # print("Hey I am a Person") 
        self.name = name 
        self.occ = occ                #dunder method

    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Person("Divya","HR")
b = Person("Harry","Developer")

a.info()
b.info()