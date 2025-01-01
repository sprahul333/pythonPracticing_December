name="Rahul"

vowels="aeiouAEIOU"

for i in name:
    if i in vowels: #Checks if the character is a vowel
        name=name.replace(i,"*")

print(name)

print("*************************************************************")

#Reversing a string using for loop:

name="Rahul"
reversedName='';

for i in range(len(name)):
    reversedName=name[i]+reversedName;

print(reversedName)

print("*************************************************************")

#WAP which will keep on adding the student until the user says no

students=[]

while True:
    student=input("Enter the student name:")
    students.append(student)
    response=input("Do you want to add another student(yes/no):")
    if response.lower()=='no':
        break

print(students)

print("*************************************************************")