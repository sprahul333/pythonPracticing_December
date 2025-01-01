# Prints the list of duplicate words in a string
str2 = "Selenium is a web automation tool which is used for automating web applications. Selenium is an open source tool"
dict2 = {};

for i in str2.split(" "):  # Reading each word from the string
    if i in dict2:  # Checking if the word is already present in the dictionary
        dict2[i] = dict2[
                       i] + 1  # If the word is already present in the dictionary, then increment the count of the word
    else:
        dict2[i] = 1  # If the word is not present in the dictionary, then add the word to the dictionary

#print(dict2)

print("*************************************************************************************************************")

duplicate_words=[]

for key, value in dict2.items():
    if (value > 1):
        duplicate_words.append(key)

print(duplicate_words)
