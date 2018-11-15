# https://www.w3schools.com/python/python_classes.asp

class Student:
    id 
    name = ""
    age = 20
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def sayHello(self):
        print("Hello my name is: " + self.name )
        print (" my id is ", self.id)
        print (" I am ", self.age, " years old")
    
s1 = Student(101, "John", 36)

print("Name: ", s1.name)
print("Id: ", s1.id)
print("Age: ", s1.age)
s1.sayHello()
