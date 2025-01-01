#Tuple is static --> Fixed size
#List is dynamic --> Dynamic Size

#Syntax of a tuple:
tuple1=("Apple","Banana","Cherry","Dates")

print(tuple1)
#Tuple is a collection of items which can be of different data types

print(len(tuple1))
print(tuple1[2])

#tuple1[2]="Mango"

print(tuple1)

#Returns the index of the element
print(tuple1.index("Banana"))

#Searching for an element in the tuple
print("Banana" in tuple1)

#Count the number of times an element is present in the tuple
print(tuple1.count("Cherry"))

#Packing and unpacking of data in a tuple
#Packing

tuple2=("Apple","Banana","Cherry","Dates")

#Unpacking

fruit1,fruit2,fruit3,fruit4=tuple2

print(fruit1)
print(fruit2)
print(fruit3)
print(fruit4)

print("***************************************************************************")

#* is used to pack the data in a tuple
fruit5, *fruit6=tuple2

print(fruit5)
print(fruit6)

print(fruit6[2])

print("***************************************************************************")

#Unpacking the data in a tuple
fruit7, *fruit8, fruit9=tuple2

print(fruit7)
print(fruit8)
print(fruit9)

print(f'Fruit 8 is: {fruit8} and fruit 9 is: {fruit9}')

print("***************************************************************************")

#Convert tuple to list
list1=list(tuple2)

print(list1)

list1.append("Mango")

print(list1)

print("***************************************************************************")

tuple3=(10,20,30,(50,60,70))

list2=list(tuple3)
list3=list2[3]

print(list2,list3)