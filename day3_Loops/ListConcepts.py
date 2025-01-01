#List Syntax:
#list1=["Apple","Banana","Cherry","Dates"]
#List is a collection of items which can be of different data types

l1=["Apple","Banana","Cherry","Dates",10,20,None,True,9.214]

#Printing the list
print(l1)

#Printing the first element of the list
print(l1[0])

#Length of the list
print(len(l1))

#Adding an element to the list
l1.append("Mango")

print(l1)

#Inserting an element at a specific position
l1.insert(2,"Orange")

print(l1)

#Removing an element from the list
l1.remove("Banana")

print(l1)

#Removing the last element from the list
l1.pop()

print(l1)

#Removing an element from a specific position
l1.pop(2)

print(l1)

#Searching for an element in the list
print("Apple" in l1)

#Prints the value at the 3rd index position
print(l1[3])

#Sorting the list -- This will throw an error as the list contains different data types
#l1.sort()

print(l1)

#Printing the list in reverse order
l1.reverse()

print(l1)

#Copying the list
l2=l1.copy()

print(l2)

#Counting the number of times an element is present in the list
print(l1.count("Apple"))

#Extending the list
#Combining two lists
l1.extend(l2)

print(l1)

#Clearing the list
l1.clear()

print(l1)

#All function --> Returns True if all the elements in the list are True
#Returns False if any of the element in the list is False
#Returns False if the list is empty
my_list = [1, 2, 3]
print(all(my_list))

#Perfoms the sum of numbers in the list
print(sum(my_list))

#Performs the sum of numbers in the list and adds 10 to it
print(sum(my_list,10))

#Copy the list
my_list1=my_list.copy()

print(my_list1)

#Max value in the list
print(max(my_list1))

#Min value in the list
print(min(my_list1))

#Index of the element in the list
print(my_list1.index(3))

#Zip function --> Combines two lists into a list of tuples
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
print(list(zipped))

#Flattening a list if it is a nested list
nested_list = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested_list for item in sublist]
print(flattened)

#List slicing in steps of 2
nums = [1, 2, 3, 4, 5, 6]
every_other = nums[::2]
print(every_other)


from collections import deque

queue = deque([1, 2, 3])
queue.append(4)  # Enqueue
print(queue.popleft())  #Remove the first element from the queue

print(queue)

import bisect

#Efficiently insert elements into a sorted list while maintaining order.
sorted_list = [1, 3, 4, 7]
bisect.insort(sorted_list, 5)
print(sorted_list)

#Generate all possible pairs from two lists
from itertools import product

list1 = [1, 2]
list2 = ['a', 'b']
cartesian_product = list(product(list1, list2))
print(cartesian_product)

#Stack using list
stack = []
stack.append(1)  # Push
stack.append(2)
# print(stack.pop())  # Pop: Output: 2
print(stack)

from collections import Counter

nums = [1, 2, 2, 3, 3, 3]
count = Counter(nums)

#Different Functions Under Counter
#Print the most common element in the list
print(count.most_common(1))

#Print the elements in the list
print(count.elements)

#Print the count of each element in the list
print(count)
