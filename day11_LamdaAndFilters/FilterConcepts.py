list1=[539,2350,23,236,235,125]

#Iteraable means the collection object
#Syntax of filter: filter(function, iterable)
#filter() function is used to filter the elements based on the condition
#list() is used to convert the filter object to list
filteredList = list(filter(lambda x: x%2==0, list1))

print(filteredList)

tools=["Selenium","Cypress","Protractor","Appium","Katalon","UFT"]

filteredList=list(filter(lambda x: x.startswith("S"),tools))

print(filteredList)

#Print the strings greater than length 5
filteredList=list(filter(lambda s:len(s)>5,tools))

print(filteredList)

age=[23,45,67,89,12,34,56,78,90]

#x>25 and x<65 --> 25<x<65
eligibleToContest=list(filter(lambda x:(x>25 and x<65),age))

print(eligibleToContest)