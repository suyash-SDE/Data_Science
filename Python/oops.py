# # class
# class Factory:
#     a = 12 #attributes

#     def hello(self): # method
#         print("How are u")

#     print("hello how are u i am getting initialized")    


# # print(Factory().a)
# # Factory().hello()

# # object
# obj= Factory()
# obj.hello()

# obj1=Factory()


# -----------

# class Factory:
#     def __init__(self,material,zips,pockets):
#         # print(self)
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets

#     def show(self): 
#         print(f"your object details are {self.material}, {self.pockets}, {self.zips}")

# reebok = Factory("leather",3,2)
# campus = Factory("nylon",3,3)

# print(reebok.material)

# reebok.show()

# class Animal:
#     name = "lion" #class attributes

#     def __init__(self,age):
#         self.age = age #instance attributes

#     def show(self):
#         print("how are u") # instance method

#     @classmethod
#     def hello(cls):
#         print("how are you brother") 

#     @staticmethod
#     def static():
#         print("how are u")



# obj = Animal(12)
# obj.show()
# obj.hello()
# obj.static()


# 4 pillor
# ----------------
# Inheritance
# class Factorymumbai:
#     a="I am an attributes mentioned inside factory"
#     def hello(self):
#         print("hello i am a method mentioned inside factory")

# class Factorypune(Factorymumbai): # child class
#     pass

# obj = Factorymumbai()
# print(obj.a)

# obj2 = Factorypune()
# print(obj2.a)

# # ----------

# single inheritance 
# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def show(self):
#         print(f"hello your name is{self.name}")

# class Human(Animal):
#     # pass
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age = age

#     def show(self):
#         print(f"hello your name is{self.name} and age {self.age}")    


# animal1 = Animal('lion')
# person1 = Human("akarsh",23)
# person1.show()


# multiple inheritance 
# class Animal:
#     name1 = "lion"

# class Human:
#     name2 = "harsh"

# class Robots(Animal,Human):
#     name3 = "charli123"

# obj = Robots()  
# print(obj.name3)  


# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Human:
#     def __init__(self, age):
#         self.age = age

# class Robots(Animal, Human):
#     name3 = "charli123"

#     def __init__(self, name, age):
#         Animal.__init__(self, name)
#         Human.__init__(self, age)

# obj = Robots("suyash", 22)

# print(obj.name)   # suyash
# print(obj.age)    # 22
# print(obj.name3)  # charli123


# This code demonstrates the concept of multiple inheritance in Python. The Animal and Human classes both define their own constructors (__init__ methods), but they are left empty using pass. The Robots class inherits from both Animal and Human, which means it can access the properties and methods of both parent classes. However, since the Robots class does not define its own constructor, Python follows the Method Resolution Order (MRO) and tries to call the constructor of the first parent class (Animal). Because the required parameters of all parent constructors are not properly handled, this results in an error when creating a Robots object. This example highlights that in multiple inheritance, constructors of parent classes are not automatically executed and must be explicitly managed in the child class.


# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Human:
#     def __init__(self, age):
#         self.age = age

# class Robots(Animal, Human):
#     robot_id = "charli123"

#     def __init__(self, name, age):
#         Animal.__init__(self, name)
#         Human.__init__(self, age)

# # Creating object
# obj = Robots("Suyash", 22)

# # Accessing attributes
# print(obj.name)      # from Animal
# print(obj.age)       # from Human
# print(obj.robot_id)  # from Robots



# 📘 What is super() in Python?

# super() is used to call a method of the parent class from a child class.
# It follows Method Resolution Order (MRO) and helps avoid duplicate calls in inheritance, especially in multiple inheritance.



# 🧠 Why use super()?

# Avoids hard-coding parent class names

# Supports multiple inheritance safely

# Cleaner and maintainable code

# Calls next class in MRO automatically


# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Human:
#     def __init__(self, age):
#         self.age = age

# class Robots(Animal, Human):
#     robot_id = "charli123"

#     def __init__(self, name, age):
#         super().__init__(name)   # calls Animal.__init__
#         Human.__init__(self, age)

# obj = Robots("Suyash", 22)

# print(obj.name)
# print(obj.age)
# print(obj.robot_id)



# class Animal:
#     def __init__(self, name, **kwargs):
#         super().__init__(**kwargs)
#         self.name = name

# class Human:
#     def __init__(self, age, **kwargs):
#         super().__init__(**kwargs)
#         self.age = age

# class Robots(Animal, Human):
#     def __init__(self, name, age):
#         super().__init__(name=name, age=age)

# obj = Robots("Suyash", 22)


# multilevel inheritance 
# ----------------------------

# class Factory:
#     def __init__(self,material,zips):
#         self.material = material
#         self.zips = zips

# class BhopalFactory(Factory):
#     def __init__(self,material,zips,color):
#         super().__init__(material,zips)
#         self.color = color      

# class PuneFactory(BhopalFactory):
#     def __init__(self,material,zips,color,pockets):
#         super().__init__(material,zips,color)
#         self.pockets = pockets        

# obj = PuneFactory()        


# hierical inheritance
# class Factory:
#     def __init__(self,material,zips):
#         self.material = material
#         self.zips = zips

# class BhopalFactory(Factory):
#     def __init__(self,material,zips,color):
#         super().__init__(material,zips)
#         self.color = color      

# class PuneFactory(Factory):
#     def __init__(self,material,zips,color,pockets):
#         super().__init__(material,zips,color)
#         self.pockets = pockets 


# polymorphism
# method overriding
# class Animal:
#     def show(self):
#         print("hello I am suyash")

# class Human(Animal):
#     def show(self):
#         print("How are you")

# obj = Human()
# obj.show()


# methodoverloading nhi hota hai python

# Duck Typing

# class Animal:
#     def show(self):
#         print("I am showing")

# class Human:
#     def show(self):
#         print("Hello I am also showing")

# obj = Animal()
# obj2 = Human()

# obj.show()
# obj2.show()

# encapsulation

# class Factory:
#     a="pune" #public
#    # _a="pune" # protected
#    #__a="pune" # private
#     def show(self):
#         print("hello i am a pune factory")

# obj = Factory()

# print(obj.a)



# class Student:
#     def __init__(self, name, age):
#         self.__name = name   # private attribute
#         self.__age = age     # private attribute

#     # Getter method
#     def get_name(self):
#         return self.__name

#     # Setter method
#     def set_name(self, name):
#         self.__name = name

#     def show(self):
#         print(f"Name: {self.__name}, Age: {self.__age}")

# # Creating object
# stu = Student("Suyash", 22)

# # Accessing private attribute using getter
# print(stu.get_name())   # Suyash

# # Modifying private attribute using setter
# stu.set_name("Rohit")
# print(stu.get_name())   # Rohit

# # Displaying all data
# stu.show()              # Name: Rohit, Age: 22


# Abstruction
# --> it not exist in python
 

# from abc import ABC, abstractmethod

# # Abstract class
# class Animal(ABC):

#     @abstractmethod
#     def sound(self):
#         pass

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")


# Great topic 👍
# Dunder methods are very important for Python internals and interviews. Let’s break it down clearly.

# 🔹 What are Dunder Methods in Python?

# Dunder = Double UNDERscore

# Dunder methods are special methods in Python that:

# Start and end with double underscores

# Example: __init__, __str__, __add__

# They are also called magic methods.

# 👉 Python calls them automatically in certain situations.

# 🔹 Why are Dunder Methods Used?

# Customize behavior of objects

# Operator overloading

# Object initialization

# String representation

# 🔹 Common Dunder Methods (Very Important)
# Method	Purpose
# __init__	Constructor
# __str__	String representation
# __repr__	Official representation
# __add__	+ operator
# __len__	len()
# __eq__	==
# __del__	Destructor
# 💻 Code Examples
# 1️⃣ __init__ (Constructor)
# class Student:
#     def __init__(self, name):
#         self.name = name

# 2️⃣ __str__ (Readable Output)
# class Student:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return f"Student name is {self.name}"

# s = Student("Suyash")
# print(s)


# Output:

# Student name is Suyash

# 3️⃣ __repr__ (Developer Output)
# class Student:
#     def __repr__(self):
#         return "Student()"

# 4️⃣ __add__ (Operator Overloading)
# class Number:
#     def __init__(self, x):
#         self.x = x

#     def __add__(self, other):
#         return self.x + other.x

# a = Number(10)
# b = Number(20)

# print(a + b)


# Output:

# 30

# 5️⃣ __len__
# class Team:
#     def __init__(self, members):
#         self.members = members

#     def __len__(self):
#         return len(self.members)

# t = Team(["A", "B", "C"])
# print(len(t))


# Output:

# 3

# 6️⃣ __eq__
# class Person:
#     def __init__(self, age):
#         self.age = age

#     def __eq__(self, other):
#         return self.age == other.age

# p1 = Person(20)
# p2 = Person(20)

# print(p1 == p2)


# Output:

# True

# 🔹 When are Dunder Methods Called Automatically?
# Action	Dunder Method
# Create object	__init__
# print(obj)	__str__
# obj1 + obj2	__add__
# len(obj)	__len__
# obj1 == obj2	__eq__
# 🧠 Interview One-Liner

# Dunder methods are special methods in Python that allow us to define custom behavior for built-in operations

# advance stuff

# custom decorator

def decorate(func):
    def wrapper():
        print("i will print myself before the function hrllo")
        fun()
        print("I will print after the function")
    return wrapper    

@decorate
def hello():
    print("hello i am suyash Sharma")

hello()