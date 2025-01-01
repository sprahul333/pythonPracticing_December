age=int(input("Enter your age"))

attendance=int(input("Enter your attendance"))

assignments=input("Enter your assignments submitted? Yes or No")

if(age>21):
    print("Age Verification Passed")

    if(attendance>80):
        print("Attendance Verification Passed")

        if(assignments=="Yes"):
            print("Assignments Verification Passed, Eligible for placements")
        else:
            print("Submit all assignments and apply again")
    else:
        print("Attendance Verification Failed")

else:
    print("Age Verification Failed")

print("********************************************************************************************************************************************")

#Nested if else

marks=int(input("Enter your marks"))

if(marks>90):
    print("Grade A")
elif(marks>80 and marks<=90):
    print("Grade B")
elif(marks>70 and marks<=80):
    print("Grade C")
elif(marks>60 and marks<=70):
    print("Grade D")
else:
    print("Grade E, failed, please focus on your studies")


print("********************************************************************************************************************************************")

#Ternary Operator

a=10
b=20

print("A is greater than B") if a>b else print("B is greater than A")


