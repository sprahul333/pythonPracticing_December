# Purpose of functions:
# 1. To demonstrate the declaration of functions in Python
# 2. To demonstrate the calling of functions in Python
# 3. To demonstrate the return type of functions in Python
# 4. To demonstrate the passing of arguments to functions in Python
# 5. To demonstrate the default arguments in functions in Python
# 6. Code reusability

# Syntax of a function:
# def function_name():
#     #Code block

# FUnction with no return type and no arguments
def display():
    print("Welcome to Python Functions")


# Calling the function
display()
display()
display()
display()

print("***************************************************************************")


# Function with return type and no arguments

def display1():
    return "Welcome to Python Functions"


# Calling the function
print(display1())
print(display1())
print(display1())

print("***************************************************************************")


# Function with return type and arguments

def display2(name):
    return f"Welcome to Python Functions {name}"


# Calling the function
print(display2("Selenium"))

print("***************************************************************************")


# Function with return type and multiple arguments

def display3(name, age):
    return f"Welcome to Python Functions {name} and your age is {age}"


# Calling the function
print(display3("Selenium", 30))


def display_name(name):
    print("Hello", name)


display_name("Selenium")
display_name("Python")

print("***************************************************************************")


def add(a, b):
    return a + b


print(add(10, 20))

print("***************************************************************************")


# Passing the default arguments
def add1(a, b=0):
    return a + b


print(add1(10))

print("***************************************************************************")


def sub(a, b):
    return a - b


print(sub(20, 10))

print("***************************************************************************")


def mul(a, b):
    return a * b


print(mul(20, 10))

print("***************************************************************************")


def div(a, b):
    return a / b


print(div(20, 10))

print("***************************************************************************")


# Variable length arguments --> Not sure how many argumments do we want
def add_number(*args):
    print(type(args))  # Prints the type of the variable --> tuple
    print(args)
    print(args[2] + args[1] + args[0])


add_number(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

print("***************************************************************************")


# Only one variable length argument is allowed in a function
# def add_number(args1,*args2):

# Variable length arguments --> Not sure how many argumments do we want
def add_number(num1, num2, *args):
    print(type(args))  # Prints the type of the variable --> tuple
    print(args)
    print(args[2] + args[1] + args[0])

    for i in args:
        print(i)


add_number(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

print("***********************************************************************************************")


# ** --> Keyword arguments
# Keyword arguments are used to pass the values to the function in the form of key value pairs

def display_details(name, age):
    print(name)
    print(age)


display_details(name="Selenium", age=30)

print("***********************************************************************************************")


def display_details1(**kwargs):
    print(kwargs)
    print(type(kwargs))
    print(kwargs["name"])
    print(kwargs["age"])
    print(kwargs["location"])


display_details1(name="Selenium", age=30, location="Bangalore")

print("***********************************************************************************************")

#We can add both the variable length arguments and keyword arguments in a function
#But only one variable length argument is allowed in a function
#But only one keyword argument is allowed in a function
def f1(num1, num2, *args, **kwargs):
    print(num1)
    print(num2)
    print(args)
    print(kwargs)


f1(10, 20, 30, 40, 50, 60, 70, 80, 90, 100, name="Selenium", age=30, location="Bangalore")

print("***********************************************************************************************")

#Default arguments
#Default arguments are used to assign the default values to the arguments in a function
#If the value is passed to the argument, then the default value is overridden
def default_paraeters(name, age=30):
    print(name)
    print(age)

default_paraeters("Selenium")
default_paraeters("Python",40)

print("***********************************************************************************************")
