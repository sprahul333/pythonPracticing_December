# Abstraction:
# 1. Abstraction is the concept of hiding the complex implementation details and showing only the necessary features of the object.
# 2. Abstraction is achieved using abstract classes and interfaces.
# 3. Abstract class is a class that contains one or more abstract methods.
# 4. Abstract method is a method that is declared but not implemented.
# 5. Abstract class cannot be instantiated.
# 6. Abstract class can have both abstract and concrete methods.


# Abstraction using Abstract class
from abc import ABC, abstractmethod


# Abstract class
# class Notifications(ABC): ---> Represents the abstract class
class Notifications(ABC):
    def m1(self):
        pass

    # Decorator --> It is used to declare the method as abstract method
    @abstractmethod
    def send(self):
        pass

    @abstractmethod
    def receive(self):
        pass


class SMS(Notifications):

    # Need to implement the abstract method of the parent class
    def send(self):
        print("SMS Method")

    def receive(self):
      print("Receive Method from SMS")


class Email(Notifications):
    def send(self):
        print("Email Method")

    def receive(self):
        print("Receive Method from Email")

    def m1(self):
        pass


sms1 = SMS()
sms1.send()
sms1.receive()

email1 = Email()
email1.send()
email1.receive()

# If we try to create an object for the abstract class, then it will throw an error
# notify=Notifications()

#Anonymous Object Creation is not there in python
# Approach works, if the class has only one method to call
SMS().send()
Email().send()
SMS().receive()
Email().receive()
