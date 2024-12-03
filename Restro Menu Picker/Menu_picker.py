 menu = {
    "samosa": 10,
    "kulcha": 20,
    "burger": 30,
    "coffee": 40,
    "tea": 50,
}

print("Welcome to Shadow Restaurant")
print("Here is Your menu:")
for item,value in menu.items():
    print(f"{item} : {value}")

order_total = 0
list_of_order_items = []
    
while True:
    another_order = input("enter ur order and \"no\" to exit: ").lower()
    if another_order == "no":
        break
    elif another_order == "yes":
        item2 = input("what u want to order next: ")
        if item2 in menu:
            if item2 in list_of_order_items:
                dup_item = input("this item is already in order list, do u want this again: (yes/no): ")
                if dup_item == "yes":
                    order_total += menu[item2]
                    list_of_order_items.append(item2)
                    print(f"the item {item2} is added to ur order again")
                else:
                   print(f"the item {item2} is not added to ur order")
            else:
                order_total += menu[item2]
                list_of_order_items.append(item2)
                print(f"the item {item2} is added to ur order")
        else:
            print(f"the item {item2} is not available")
    else: 
        print("please enter yes or no")

print(f"the items u have ordered are: {list_of_order_items}")
print(f"The total amount to needed to pay is: {order_total}")

