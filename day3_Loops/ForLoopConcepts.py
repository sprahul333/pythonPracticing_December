#Syntax of for loop:
#for variable in sequence:
#    statements

#Printing numbers from 1 to 10
for x in range(1,10):
    print(x)

print("**************************************************************************************")

#Syntax of creating a list
list1=["Apple","Banana","Cherry","Dates"]

for i in list1:
    print(i)

print("**************************************************************************************")

listProgrammingLanguages=["Python","Java","C","C++","C#","Ruby","Perl","Scala","Kotlin","Swift"]

for i in listProgrammingLanguages:
    if(i == "Python"):
        print("Python is present in the list")
    else:
        print("Python is not present in the list")

print("**************************************************************************************")

#Print the list of odd numbers from 1 to 10
for i in range(1,10):
    if(i%2!=0):
        print(i)

print("**************************************************************************************")

#Find the sum of all the numbers from 1 to 10

sum=0
for i in range(1,10):
    sum+=i

else: #This block will be executed after the for loop is completed
    print("Completed")

print(sum)

print("**************************************************************************************")

#Print the numbers from 1 to 10 by skipping 2 numbers
for i in range(1,10,2):
    print(i)

print("**************************************************************************************")

#Print the numbers from 10 to 1

# -1 is the step value which will decrement the value of i by 1
for i in range(10,0,-1):
    print(i)

print("**************************************************************************************")

for i in range(2,20,3):
    print(i)

print("**************************************************************************************")

#Print the numbers from 1 to 10 in reverse order

for i in range(10,0,-1):
    print(i,end="\t")

print("**************************************************************************************")

#Handling String using for loop

string="Python"

for i in string:
    if(i == "t"):
        print("t is present in the string")
    else:
        print(i)

print("**************************************************************************************")



