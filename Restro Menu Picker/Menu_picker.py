'''
#simple code


menu_list = {
    "burger": 50,
    "milk shake": 90,
    "coffee" : 150,
    "noodles" : 200,
    "samosa": 40
    }
print("Welcome to Python Restaurant")
print("Here is your menu: ")
print("burger: 50\nmilk shake: 90\ncoffee : 150\nnoodles : 200\nsamosa: 40")

order_total = 0
item_1 = input("Enter the item that u want to order: ")
if item_1 in menu_list:
    order_total += menu_list[item_1]
    print(f"Here ur {item_1} is added to ur order")
else:
    print(f"the ordered item {item_1} is not available yet")
    
another_order = input("Do u want to add another order (yes/no)")
if another_order == "yes":
    item_2 = input("Enter ur another order: ")
    if item_2 in menu_list:
        order_total += menu_list[item_2]
        print(f"Second item {item_2} is added to ur order")
    else:
        print(f"The item {item_2} is not available yet")

print(f"\nThe total amount of ur order is: {order_total}")

'''  








'''

#code with loop

menu = {
    "samosa": 10,
    "kulcha": 20,
    "burger": 30,
    "coffee": 40,
    "tea": 50,
}

print("Welcome to Shadow Restaurant")
print("Here is Your menu:")
print("samosa: 10\nkulcha: 20\nburger: 30\ncoffee: 40\ntea: 50")

order_total = 0

# First order
item_1 = input("Enter your first order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Item {item_1} is added to your order")
else:
    print(f"Item {item_1} is not available")

# Loop for additional items
while True:
    another_item = input("Do you want to order anything else (yes/no): ").lower()
    if another_item == "no":
        break
    elif another_item == "yes":
        item_2 = input("What do you want to order: ")
        if item_2 in menu:
            order_total += menu[item_2]
            print(f"Item {item_2} is added to your order")
        else:
            print(f"Item {item_2} is not available")
    else:
        print("Please answer with 'yes' or 'no'.")

# Final total
print(f"Here is your total amount to pay: {order_total}")


'''  







  
'''

#short form of a code

menu = {
    "samosa": 10,
    "kulcha": 20,
    "burger": 30,
    "coffee": 40,
    "tea": 50,
}

order_total = 0
print("Welcome to Shadow Restaurant")
print("Here is Your menu:")

for item,price in menu.items():
    print(f"{item} : {price}")

while True:
    item = input("Enter ur order (or type \"no\" to exit) ")
    if item == "no":
        break
    elif item in menu:
        order_total += menu[item]
        print(f"Item {item} is added to ur order")
    else:
        print(f"Item {item} is not available")

print(f"Here is ur total amount to pay: {order_total}")
    
'''
    




'''

menu = {
    "samosa": 10,
    "kulcha": 20,
    "burger": 30,
    "coffee": 40,
    "tea": 50,
}

print("Welcome to Shadow Restaurant")
print("Here is Your menu:")
print("samosa: 10\nkulcha: 20\nburger: 30\ncoffee: 40\ntea: 50")

order_total = 0
list_of_order_items = []

item1 = input("enter ur first order: ")
if item1 in menu:
    order_total += menu[item1]
    list_of_order_items.append(item1)
    print(f"The item {item1} is added to ur order")
else:
    print(f"The item {item1} is not available")
    
while True:
    another_order = input("Do u want order anything else: (yes/no)").lower()
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





'''


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

