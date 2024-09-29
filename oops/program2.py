class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def __str__(self):
        return f"{self.name}({self.age})"
    
    def myfunc(abc):
        print(f"Hello my name is : {abc.name}")
        
p1=Person("Shreyash",19)
# p1.age=49
# del p1.age
p1.myfunc()
# print(p1.age)
print(p1)
# print(f"Name; {p1.name}  Age: {p1.age}")