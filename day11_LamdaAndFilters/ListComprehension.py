#List Comprehension:

#Purpose: To create a new list by applying an expression to each item in an existing list.

#Syntax: [expression for item in iterable]

#Example 1:

oldList=[1,2,3,4,5,6,7,8,9,10]

newList=[x*x for x in oldList]

print(newList)

newListOldWay=[]
#Old way is:

for i in oldList:
    newListOldWay.append(i*i)

print(newListOldWay)

#Example 2:

oldSet={1,2,3,4,5,6,7,8,9,10,20,30,10,20,30}

newSet={x*2 for x in oldSet}

print(newSet)

#Example 3:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Find the even numbers from the list

#Syntax using if condition: [expression for item in iterable if condition]
evenNumbers=[x for x in numbers if x%2==0]

print(evenNumbers)

#More than one condition

#Syntax: [expression for item in iterable if condition1 and condition2]

evenNumbers=[x for x in numbers if x%2==0 and x%3==0]

print(evenNumbers)