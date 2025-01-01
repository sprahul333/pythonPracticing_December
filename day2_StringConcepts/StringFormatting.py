data="Selenium"

typeOfTool="Free"

print("The tool "+data+" is "+typeOfTool)

print(f'The tool {data} is {typeOfTool}')

#Another way of formatting the string
name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))

#Another way of formatting the string
#The order of the variables can be changed
print("{1} is older than {0}".format("John", "Alice"))  # Output: Alice is older than John

#Named Placeholders
print("{name} is {age} years old.".format(name="Bob", age=22))  # Output: Bob is 22 years old.


from string import Template

template = Template("Hello, $name!")
print(template.substitute(name="Emma"))  # Output: Hello, Emma!

#Another way of formatting the string
#$$$ is used to escape the dollar sign
template = Template("The price of $item is $$${price}")
print(template.substitute(item="apple", price=2.5))  # Output: The price of apple is $2.5


text = "Hello"

#<10 is used to left-align the text within a width of 10
print("{:<10}".format(text))

#>10 is used to right-align the text within a width of 10
print("{:>10}".format(text))

#^10 is used to center-align the text within a width of 10
print("{:^10}".format(text))


#.2f is used to format the float value to 2 decimal places
#15 is used to right-align the text within a width of 15 with a whitespace padding
value = 123.456
print(f"Value: {value:.2f}".rjust(15))  # Output: "       Value: 123.46"

#Mutltiline String formatting:

name = "John"
age = 30
info = f"""
Name: {name}
Age: {age}
"""
print(info)

#Displaying the binary, octal, and hexadecimal values of a number
number = 42
print(f"Binary: {number:b}, Octal: {number:o}, Hex: {number:x}")

#Displaying the number with commas
value = 123456789
print(f"Formatted: {value:,}")

#Displaying the number with a width of 10
#The value is right-aligned
width = 10
value = 42
print(f"Value: {value:{width}}")

