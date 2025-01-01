class Student:
    def __init__(self): #Default constructor
        self.name="Selenium"
        self.age=30
        self.marks=90
        self.location="Bangalore"
        self.paidFees=True
        self.coursesTaken=[]

    #self is a reference variable which is used to refer the current object
    #Self is used to access the instance variables and methods of the class
    #Self is used to create the instance variables and methods of the class
    #Instead of self, we can use any other name also, but self is the standard name used in python
    #self should be the first parameter in the constructor and methods of the class
    #If it is not the first parameter, then it will throw an error
    def __init__(self,name,age,marks,location,paidFees,courses): #Parameterized constructor
        self.name=name
        self.age=age
        self.marks=marks
        self.location=location
        self.paidFees=paidFees
        self.coursesTaken=courses

    def display(self):
        # print(self.name)
        # print(self.age)
        # print(self.marks)
        # print(self.location)
        # print(self.paidFees)
        print(f'Name: {self.name}, Age: {self.age}, Marks: {self.marks}, Location: {self.location}, Paid Fees: {self.paidFees}')

        print("List of Courses Taken:")
        for course in self.coursesTaken:
            print("Course Taken: ",course)


#If we have both default and parameterized constructors, then during the object creation, the parameterized constructor will be called

student1=Student("Python",40,100,"Chennai",False,["Selenium","Java","Python"])
print(student1.name)

student1.display()

print("***********************************************************************************************")
student1.paidFees=False

student1.display()

print("***********************************************************************************************")

result=min(15,23)
print(result)