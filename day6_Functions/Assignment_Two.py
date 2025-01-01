def shopping_list(*items):

    if(len(items)==0):
        print("No Items in the shopping list")

    else:
        for item in items:
                print(item)

item=input("Enter the items ('or done to finish')")
items=[];

while item.lower()!='done':
    items.append(item)
    item=input("Enter the items ('or done to finish')")

shopping_list(*tuple(items))