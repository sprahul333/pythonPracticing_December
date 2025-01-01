#This is a template for creating a class and objects
class Student:
    name="Selenium"
    age=30
    marks=90
    location="Bangalore"
    paidFees=True

#Syntax for creating an object
#object_name=Class_name()

student1=Student()

#Accessing the class variables using the object
print(student1.name)
print(student1.age)
print(student1.marks)
print(student1.location)

#Can access the variable and modify the data
student1.location="Chennai"

print(student1.location)
