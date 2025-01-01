def grocery_bill(** items):
    total = 0
    for key, value in items.items():
        total += value
    return total


itemDetails=input("Enter the Item Name('or done to finish')")
itemPrice=float(input(f'Enter the Item Price for {itemDetails}'))

items={}

while itemDetails.lower()!='done':
    items.update({itemDetails:itemPrice})
    itemDetails=input("Enter the Item Name('or done to finish')")

    if itemDetails.lower() != 'done':
        itemPrice = float(input(f'Enter the Item Price for {itemDetails}'))

print(f'Total Bill Generated is: "{grocery_bill(**items)}"')



