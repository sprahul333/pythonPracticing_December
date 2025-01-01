name="Selenium"

#Prints the character at 7th index position
print(name[7])

#Prints the string in capital letters
print(name.upper())

#Prints the string in lower case letters
print(name.lower())

#Prints the length of the string
print(len(name))

#Prints the string starting from 0th index to 4th index
#Slicing Technique
print(name[0:4])

#Prints the index of the character 'e' in the string
print(name.find('e'))

#Prints the string starting from 2nd index to the end of the string
print(name[2:])

#Prints the string starting from 0th index to 5th index
print(name[:5])

#Prints the string starting from 0th index to the end of the string
print(name[:])

#Prints the string starting from 0th index to the end of the string with a step of 2
print(name[0:8:2])

#Prints the string starting from 0th index to the end of the string with a step of 3
print(name[0:len(name):3])

name1="Selenium is a web automation tool and web founded by Jason Huggins in 2004"

#Splits the string on the basis of white spaces
print(name1.split(" "))

#Counts the number of times the word 'web' is present in the string
print(name1.count("web"))

name2="            JAVA CODING              "

#Removes the white spaces present at the start and at the end of the string
print(name2.strip())

#Removes the white spaces present at the start of the string
print(name2.lstrip())

#Removes the white spaces present at the end of the string
print(name2.rstrip())

#Replaces the word 'JAVA' with 'PYTHON'
print(name2.replace("JAVA","PYTHON"))

name3="Selenium is an automation tool"

#Checks if the string starts with 'Selenium'
#Case Sensitive matters here
print(name3.startswith("Selenium"))

#Checks if the string starts with 'Selenium' from the 6th index
print(name3.startswith("Selenium",6))

#Checks if the string ends with 'tool'
#Case Sensitive matters here
print(name3.endswith("tool"))

#Checks if the string ends with 'tool' from the 6th index
print(name3.endswith("tool",6))

#Checks if the string contains the word 'automation'
#Case Sensitive matters here
print("automation" in name3)
print("Automation" in name3)

name4="Selenium"
name5="SelEnium"

#Checks if the two strings are equal
print(name4==name5)

#Checks if the two strings are not equal
print(name4!=name5)

#Checks if the two strings are equal ignoring the case
print(name4.lower()==name5.lower())

#Reverses the string
#:: is used to reverse the string
#-1 is used to reverse the string
print(name4[::-1])

#Swap the Cases of the string
#Converts the lower case letters to upper case letters and upper case letters to lower case letters
print(name4.swapcase())

#Checks if the string is a digit
print(name4.isdigit())

#Checks if the string is an alphabet
print(name4.isalpha())

#Checks if the string is an alphanumeric
print(name4.isalnum())

name4="selenium training"
#Converts the first character of the string to upper case
print(name4.capitalize())

#Joins the words in the list with a space
words = ["hello", "world"]
print(" ".join(words))

#Joins the words in the list with a comma
words = ["hello", "world"]
print(",".join(words))

#Left-aligns the string within a specified width
text = "hello"
print(text.ljust(10, '-'))

#Right-aligns the string within a specified width
text = "hello"
print(text.rjust(10, '-'))

#Center-aligns the string within a specified width
text = "hello"
print(text.center(10, '-'))

#pads the string with zeros at the start
text = "42"
print(text.zfill(5))

#Checks if the string is a title
text = "Hello World"
print(text.istitle())

#Checks if the string is a space
text = " "
print(text.isspace())

#Maps the values in the dictionary to the string
data = {"name": "John", "age": 30}
text = "My name is {name} and I am {age} years old."
print(text.format_map(data))

#IsIdentifier --> Checks if the string is a valid identifier
#What is an identifier?
#An identifier is a name given to entities like class, functions, variables, etc. It helps to differentiate one entity from another.
text = "hello_world"
print(text.isidentifier())  # Output: True

text = "123hello"
print(text.isidentifier())

#Checks if the string is a printable
text = "Hello World"
print(text.isprintable())

#Checks if the string is a decimal
text = "123"
print(text.isdecimal())

#Checks if the string is a numeric
text = "123"
print(text.isnumeric())

#Removes the prefix from the string
text = "prefix_text"
print(text.removeprefix("prefix_"))

#Removes the suffix from the string
text = "text_suffix"
print(text.removesuffix("_suffix"))

#Checks if the string is an ascii
text = "hello"
print(text.isascii())

#Checks subsets of the string
a = set("hello")
b = set("hello world")
print(a.issubset(b))

#Checks supersets of the string
a = set("hello")
b = set("hello world")
print(b.issuperset(a))

#Encodes a string into bytes using a specified encoding.
text = "hello world"
print(text.encode('utf-8'))

#Translate the string based on the mapping table

#The translate() method returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table.

text = "hello"
table = str.maketrans('aeiou', '12345')
print(text.translate(table))


table = str.maketrans({'a': '1', 'e': '2'})
print("apple".translate(table))

#Splits the string into lines based on the line separator
text = "Hello\nWorld\nPython"
print(text.splitlines())

#CaseFold --> Converts the string into lower case
#Difference between .lower() and .casefold() is that .casefold() is stronger than .lower()
#It converts more characters to lower case
text1 = "straße"
text2 = "STRASSE"
print(text1.casefold() == text2.casefold())

#ExpandTabs --> Expands the tabs in the string
text = "hello\tworld"
print(text.expandtabs(4))

#Partition --> Splits the string into three parts based on the separator
text = "abababab"
substring = "aba"
count = sum(1 for i in range(len(text)) if text.startswith(substring, i))
print(count)