class Person:
    def __init__(self,name,age):
       self.name=name
       self.age=age

    def printfunc(self):
        print(f"Name: {self.name} Age: {self.age}")

class Student(Person):
    def __init__(self, name, age,year):
        super().__init__(name, age)
        self.graduation=year
    def welcome(self):
        print(f"Welcome {self.name} to the class of {self.graduation}.")

x=Student("Shreyash",34,2027)
x.welcome()