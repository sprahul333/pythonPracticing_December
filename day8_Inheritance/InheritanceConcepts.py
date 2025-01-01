# Desc: This file contains the code for the Inheritance concepts in Python
#: Inheritance is a mechanism in which one class acquires the properties and behavior of another class
#(): The class which is getting inherited is called as Parent class or Super class or Base class
class Parent:
    def m1(self):
        print("Parent Method")

#Method OVerloading is not supported in Python as the method with the same name will be considered as the latest method
#Method Overriding is supported in Python via Inheritance
#Method Overriding: If the child class has the same method as the parent class, then the child class method will be called
#Method Overriding is a Run Time Polymorphism
class Child(Parent):
    def m2(self):
        print("Child Method")

    def m1(self):
        super().m1() #Accessing the parent class method using super keyword
        print("Overridden Method from child")


obj1=Child()
obj1.m1()
obj1.m2()

