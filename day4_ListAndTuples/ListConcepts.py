l1=[420,20,-204,True,9.214,None, 12,12,40,-5032]

print(len(l1)) #Length of the list

print(l1[4]) #Printing the 5th element of the list

# Adding an element to the list at the end
l1.append("Mango")

print(l1)

# Inserting an element at a specific position
l1.insert(2,"Orange")

l2=["Cypress","Pine","Maple","Oak","Birch","Cedar"];

#Sorts the data in ascending order
l2.sort();

print(l2)

#Reverse the data in the list
l2.reverse();

print(l2)

#Iterate over the list:

for i in l2:
    print(i)

print("*************************************************************")

#Another way of iterating over the list

for i in range(len(l2)):
    print(l2[i])

print("*************************************************************")

#Removing an element from the list at 3rd index position
l2.pop(3)

print(l2)

l3=[200,1200,24,12,421,-2349,21]

print(l3)

#Prints the element that is removed from the list at the last index position
print(l3.pop())

print(l3)

l4=["Cypress","Selenium","IDE","Playwright","Tosca","WOIO",["Zelenium","Halenium","Selenoide"]]

print(l4)

#Prints the element at the 6th index position
print(l4[6])

#Prints the element at the 6th index position and then prints the element at the 1st index position of the list present at the 6th index position
print(l4[6][1])

l1sub=l4[6]

print(l1sub)

#Extend the list --> Adds the elements of the list to the existing list
l1sub.extend(["TestRigor","TestProject","TestCraft"])

print(l1sub)

#Erases the complete data from the list
l1sub.clear();

#Deleting the list ---> List will be deleted from the memory completely
del l1sub

#Prints the list after deleting the list
#print(l1sub)