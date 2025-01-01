
#Questions:
#1. Read the data from the file
#2. Find the duplicate the words in the file
#3. Find the words thhat are duplicate in the file and write the count of it to another file

#Solution:

#1. Read the data from the file

f=open("sample.txt","r")

content=f.read()

print(content)

#2. Find the duplicate the words in the file

words=content.split(" ")

print(words)

f.close()

wordCount={}

for word in words:
    if word in wordCount:
        wordCount[word]+=1
    else:
        wordCount[word]=1

print(wordCount)


#3. Find the words thhat are duplicate in the file and write the count of it to another file

#Creates the file during write mode if it does not exist
f1=open("output.txt","w")

for word,count in wordCount.items():
    if count>1:
        f1.write(word+" "+str(count))
        f1.write("\n")
        f1.close()

f1=open("output.txt","r")
print(f1.read())

f1.close()

#Remove the file

import os
os.remove("output.txt") #Removes the file

open("output").mkdirs() #Creates the directory

#os.rmdir("output") #Removes the directory

import shutil

# shutil.rmtree("output") #Removes the directory along with the files
