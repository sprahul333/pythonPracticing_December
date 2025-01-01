#Lamdas : One line functions
#Syntax: lambda arguments: expression

#Example 1:

addition=lambda a,b:a+b
print(addition) #<function <lambda> at 0x0000020D3D3A3D30>
print(addition(10,20))

def add(a,b):
    return a+b

# print(add(10,20))

#Example 2:

isEven=lambda a:a%2==0

print(isEven(10))

#Example 3:

def isEven1(a):
    return a%2==0

print(isEven1(10))

#Example 4:

isDivisbleBy2 = lambda a:a%2==0

print(isDivisbleBy2(10))