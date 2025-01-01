import traceback
import CustomExceptions
#Exception Handling: It is a mechanism to handle runtime errors such as divide by zero error, file not found error, etc.
#Types of Exceptions:
#1. Built-in Exceptions: These are the exceptions which are raised automatically by the python interpreter
#2. User-defined Exceptions: These are the exceptions which are raised by the user

#Built-in Exceptions:
#1. ZeroDivisionError: It is raised when we try to divide a number by zero
#2. FileNotFoundError: It is raised when we try to open a file which is not present in the specified location
#3. TypeError: It is raised when we try to perform an operation on the data type which is not supported
#4. ValueError: It is raised when we try to perform an operation on the data type which is not supported
#5. IndexError: It is raised when we try to access an index which is not present in the list
#6. KeyError: It is raised when we try to access a key which is not present in the dictionary
#7. NameError: It is raised when we try to access a variable which is not defined
#etc...


#Parent class for all the exceptions is BaseException

#Syntax of try-except block:
# try:
#     #Code which may raise an exception
# except ExceptionName:
#     #Code which will be executed when an exception is raised
#finally:
#     #Code which will be executed irrespective of the exception

try:
    num1 = int(input("Enter the first number:"))

    # ValueError: If we enter a string value, then it will throw an error
    # ZeroDivisionError: If we enter the second number as zero, then it will throw an error
    num2 = int(input("Enter the second number:"))

    quotient = num1 / num2
    print("Quotient is:", quotient)

    #as --> It is used to store the exception object in a variable
    #zero --> It is the variable name

#If the parent class exception is written at the start, then the subsequent child class exceptions will not be executed
#Does not throw an error called as unreachable code
# except BaseException as be:
#     print("Base Exception occurred:", be)
#     traceback.print_exc()
except ZeroDivisionError as zero:
    print("Cannot divide a number by zero")
    traceback.print_exc() #It is used to print the stack trace of the exception
except ValueError as v:
    print("Enter only integer values")
    raise CustomExceptions("Custom Exception")
except Exception as e:
    print("Exception occurred:", e)
else: #Purely optional
    #Code which will be executed when there is no exception
    print("Else block")
finally:
    #Resource Cleanup Code
    print("Finally block")

