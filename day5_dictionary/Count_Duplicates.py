str1 = "Hello"

# Prints the list of duplicate characteres in the string using dictionary

dict1 = {}

for i in str1:  # Reading each character from the string
    if i in dict1:  # Checking if the character is already present in the dictionary
        dict1[i] = dict1[
                       i] + 1  # If the character is already present in the dictionary, then increment the count of the character
    else:
        dict1[i] = 1  # If the character is not present in the dictionary, then add the character to the dictionary

print(dict1)

# Prints the list of duplicate words in a string
str2 = "Selenium is a web automation tool which is used for automating web applications. Selenium is an open source tool"
dict2 = {};

for i in str2.split(" "):  # Reading each word from the string
    if i in dict2:  # Checking if the word is already present in the dictionary
        dict2[i] = dict2[
                       i] + 1  # If the word is already present in the dictionary, then increment the count of the word
    else:
        dict2[i] = 1  # If the word is not present in the dictionary, then add the word to the dictionary

print(dict2)

print("*************************************************************************************************************")
# Prints the list of key value pairs in the dictionary

for key, value in dict2.items():
    print(key, value)

print("*************************************************************************************************************")

# Prints the list of keys value pairs whose value is greater than 1

for key, value in dict2.items():
    if (value > 1):
        print(key, value)

print("*************************************************************************************************************")

list3=[20,20,40,240,2934]

#Printing the list of unique numbers in the list

for i in list3: #Iterating through the list
    if list3.count(i)==1: #Checking if the number is present only once in the list
        print(i) #Printing the number

print("*************************************************************************************************************")
