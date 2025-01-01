# Dictionary:
# 1. Dictionary is a collection of key-value pairs.
# 2. Dictionary is mutable.
# 3. Dictionary is unordered.
# 4. Dictionary is indexed.
# 5. Can have duplicate values but not duplicate keys.
# 6. Dictionary can contain different data types.

# Syntax of creating a dictionary:

dict1 = {};

print(type(dict1))

dict1 = {1: "Selenium", 2: "Python", 3: "Playwright", 4: "PyTest", 5: "TeamCity", 2: "Ruby", 6: "PyTest"}

print(dict1)

# Print the value based on the key:
print(dict1[2])

# print the list of keys present in dicrtionary:
print(dict1.keys())

# print the list of values present in dictionary:
print(dict1.values())

# print the size of the dictionary:
print(len(dict1))

#Update the value of a key:
dict1[2] = "Java"

print(dict1)

#Add a new key-value pair to the dictionary if the key does not exist
#else it will update the existing key value pair
dict1.update({7: "Cypress"})

print(dict1)

dict1.update({"Mobile_Automation":"Appium"})

print(dict1)

dict1.update({"Mobile_Automation":"WebDriverIO"})

print(dict1)

#Removes the Key-Value pair from the dictionary based on the key
dict1.pop("Mobile_Automation")

print(dict1)

#Removes the last key-value pair from the dictionary
dict1.popitem()

print(dict1)

#Prints the value of the key if the key is present
#If the key is not present it will print None
print(dict1.get(200))

#Sets the value of the key value pair if the key is not present in the map
dict1.setdefault(3, "Selenium")

print(dict1)
#Erases the data from the list
dict1.clear()

print(dict1)

#Nested Dictionary and Nested Lists
dict1={"fname":"BAC","lname":"XYZ","age":30,"address":{"city":"Bangalore","state":"Karnataka","country":"India","pincode":560001},
       "offers":["Offer1","Offer2","Offer3","Offer4","Offer5"]}

print(dict1)

#Prints the value of the key present in the dictionary
print(dict1["fname"])

localAddress={"city":"Bangalore","state":"Karnataka","country":"India","pincode":560001}
listOfOffers=["Offer1","Offer2","Offer3","Offer4","Offer5"]

#Nested Dictionary and Nested Lists with variables
dict1={"fname":"BAC","lname":"XYZ","age":30,"address":localAddress,"offers":listOfOffers}

#Print the second offer from the list of offers
print(dict1["offers"][1])

#Prints the city from the address
print(dict1["address"]["city"])