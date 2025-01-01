#Set is a collection of unique elements
#Set is mutable
#Set is unordered
#Set is indexed
#Set can contain different data types

set1={40,20,420,12,512,23,40}

print(set1)

#Adds an element to the set
set1.add(500)

print(set1)

#Removes an element from the set
set1.remove(40)

print(set1)

#Iterate over the set:

print("*****************************************************************************")

for i in set1:
    print(i)

print("*****************************************************************************")

#Removes the first element from the set
set1.pop()

print(set1)

#Adds the value to the set randomly
set1.update("2")

print(set1)


#Convert the set to list:

list1=list(set1)

print(list1)

#Prints the element at the 3rd index position
print(list1[2])

#Converts the list to set:

set2=set(list1)
print(set2)