#Map is used to apply the function to all the elements of the iterable

oldList=[1,2,3,4,5,6,7,8,9,10]

newList=list(map(lambda x:x*x, oldList))
print(newList)

oldSet={1,2,3,4,5,6,7,8,9,10,20,30,10,20,30}

newSet=set(map(lambda x:x*x, oldSet))

print(newSet)

#Order the data in the set

#Sorted is used to sort the data in ascending order
orderedSet=set(sorted(map(lambda x:x*x, oldSet),reverse=False))

print(orderedSet)



