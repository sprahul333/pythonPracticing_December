itinerary=["Chennai","Bangalore","Pune","Delhi","Goa"]

print(itinerary)

new_city=input("Enter the city you want to add to the itinerary")

itinerary.insert(2,new_city)

print(itinerary)

city_toBe_removed=input("Enter the city you want to remove from the itinerary")

if( city_toBe_removed in itinerary):
    print("City Exists")
else:
    print("City to be removed does not exist")

itinerary.remove(city_toBe_removed)

print(itinerary)
