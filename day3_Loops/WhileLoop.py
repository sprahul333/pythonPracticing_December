#Syntax of while loop:

#while condition:
#    statements
#The while loop will execute the statements inside the block as long as the condition is true.
# Once the condition becomes false, the loop will exit.

i=1;
while i<=10:
    print(i)
    i+=1

else:
    print("Completed")
print("*****************************************************************")

#Example 2:

i=10;

while i>=0:
    print(i)
    i=i-1;
else:
    print("Completed")

print("*****************************************************************")

#Example 3:

i=1

while i<=100:
    print(i)
    i=i*10

else:
    print("Loop Completed")

#Example 4:

name="Looping Concepts"

while(len(name)>0):
    print(name)
    name=name[1:]

else:
    print("*****************************************************************")
    print("Loop Completed")

print("*****************************************************************")

#Example 5:

#Pattern Printing

i=1

while i<=5:
    print("*"*i)
    i+=1

else:
    print("Pattern Printing Completed")


#Example 6:

i=10

while i>=0:
    print("*"*i)
    i-=1

else:
    print("Pattern Printing Completed")

#Example 7:

i=1

while i<=5:
    print(" "*(5-i)+"*"*i)
    i+=1

else:
    print("Pattern Printing Completed")

