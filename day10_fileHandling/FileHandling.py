#input libraries will help us read text based file, .config file, .json files etc.

#For Excel files, we need to install openpyxl library
#For PDF files, we need to install PyPDF2 library
#For Word files, we need to install python-docx library
#For CSV files, we need to install csv library

#Syntax of open:
#open('filename','mode') --> It is used to open a file

#By Default, the file will be opened in read mode
fileObject=open("sample.txt")

print(fileObject)

#To read the complete content of the file
content=fileObject.read()
print(content)

#Takes the first line of the file
content=fileObject.readline()
print(content)

#Takes the second line of the file
content=fileObject.readline()
print(content)

#Opens the file in write mode
f=open("sample.txt","w")

#Writes the content to the file
f.write("Hello World")
f.write("\n")
f.write("Welcome to Python")

#Closes the file to avoid memory leakage
f.close()

#Cannot perform any file operations as the file is closed
# f.write("Hello World")

f=open("sample.txt","r")

print(f.read(2)) #Reads the first 2 characters of the file

print(f.read(5)) #Reads the next 5 characters of the file

import os
print(os.getcwd()) #It is used to get the current working directory

#It is used to get the directory of the file
print(os.path.dirname(__file__))

#It is used to get the complete path of the file
print(os.path.join(os.path.dirname(__file__),"..","sample.txt"))

