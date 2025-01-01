#Multiple Inheritance
class Parent1:
    def display(self):
        print("Parent1 Method")

class Parent2:

    def display(self):
        print("Parent2 Method")

class Child(Parent1,Parent2):
    def display(self):
        super().display()
        print("Child Method")

child1=Child()
child1.display()


#When there is multiple Inheritance, the method of the first parent class will be called
#Method Resolution Order (MRO) is the order in which the method will be called in case of multiple inheritance