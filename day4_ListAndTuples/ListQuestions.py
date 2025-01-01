evennumber=[];
oddnumber=[];

for num in range(1,20):
    if num%2==0:
        evennumber.append(num)
    else:
        oddnumber.append(num)

print(evennumber)
print(oddnumber)

#Modifying the list at the 2nd index position
evennumber[2]=100

print(evennumber)


#Store all the prime numbers between 1 to 100 in a list

# num1=int(input("Enter your range of numbers"))
#
# for i in range(1,num1):
#     if i%i==0 & i%1==0:
#         print("Not a prime number: "+str(i))
#     else:
#         print("Prime number: "+str(i))

#Store all the prime numbers between 1 to 100 in a list

num1=int(input("Check whether the given number is prime or not"))

evennumber=[]
nonprimenumbers=[]


for num_check in range(1,num1):
    if(num_check>0):
        for i in range(2,num_check):
            if num_check%i==0:
                # print("Not a prime number: "+str(i))
                nonprimenumbers.append(num_check)
                break;
        else:
            evennumber.append(num_check)
            # print("Prime number: "+str(i))
    else:
        print("Enter a valid number")

print(evennumber)

#List are mutable
#List can contain different data types
#List can contain duplicate values
#List can contain nested lists
#List can be modified
#List can be sorted


#Tuple are immutable
#Tuple can contain different data types
#Tuple can contain duplicate values
#Tuple can contain nested tuples
#Tuple can not be modified
#Tuple can not be sorted

#List is represented by []
#Tuple is represented by ()
