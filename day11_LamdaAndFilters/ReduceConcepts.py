#Use Cases of Reduce:

#1. Find the maximum of a list of values
#2. Find the sum of a list of values
#3. Find the product of a list of values

#Syntax: reduce(function,iterable)

#Reduce is used to reduce the iterable to a single value

#Example 1:

from functools import reduce

list1=[1,2,3,4,5,6,7,8,9,10]

maxValue=reduce(lambda a,b:a if a>b else b, list1)

print(maxValue)

sumValue=reduce(lambda a,b:a+b, list1)

print(sumValue)