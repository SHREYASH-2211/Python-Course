class Person:
    def __init__(self,name,age):
       self.name=name
       self.age=age

    def printfunc(self):
        print(f"Name: {self.name} Age: {self.age}")

class Student(Person):
    pass

x=Student("Shreyash",34)
x.printfunc()