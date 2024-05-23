# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered

order_list = []


print("Welcome to the variety food truck.")


place_order = True

while place_order:
    
    print("From which menu would you like to order? ")

    i = 1
    
    menu_items = {}


    for key in menu.keys():
        print(f"{i}: {key}")
       
        menu_items[i] = key
       
        i += 1

    
    menu_category = input("Type menu number: ")

   
    if menu_category.isdigit():
       
        if int(menu_category) in menu_items.keys():
            
            menu_category_name = menu_items[int(menu_category)]
            
            print(f"You selected {menu_category_name}")

            
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            item_selection = input("What is the menu item number? ")

            # 3. Check if the customer typed a number
            if item_selection.isdigit():
                # Convert the menu selection to an integer
                item_selection_number = int(item_selection)

                # 4. Check if the menu selection is in the menu items
                if item_selection_number in menu_items.keys(): 
                    # Store the item name as a variable
                    item_selection_name = menu_items[item_selection_number]

                    # Ask the customer for the quantity of the menu item
                    quantity = input(f"How many {item_selection_name['Item name']} would you like?" )

                    # Check if the quantity is a number, default to 1 if not
                    if not quantity.isdigit():
                        quantity = 1 
            
                    else:
                        quantity = int(quantity)
                
                    order_list.append({
                        "Item name": item_selection_name["Item name"],
                        "Price": item_selection_name["Price"],
                        "Quantity": quantity
                        })


                    # Tell the customer that their input isn't valid
                else:
                     print("Sorry your selection isn't valid")

                # Tell the customer they didn't select a menu option
            else:
               print("You did not select a menu item number.") 
        else:
            # Tell the customer they didn't select a menu option
                print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input
        match keep_ordering.lower():
                
            case 'y':
               
                place_order = True
                break
                
            case 'n':
               
               place_order = False
               print("Thank you for you order.")
               break

            case _:
                print("Sorry I do no understand. Please try again")

print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order

print(order_list)

print("Item name                 | Price  | Quantity")
print("-" * 26 + "|" + "-" * 8 + "|" + "-" * 11)

# 6. Loop through the items in the customer's order
total_price = 0

for item in order_list:
    # 7. Store the dictionary items as variables
    item_name = item['Item name']
    item_price = item["Price"]
    item_quantity = item["Quantity"]

    # 8. Calculate the number of spaces for formatted printing
    table_price = f'${item_price:.2f}'
    print(f"{item_quantity}x{item_name:<30}{table_price:>8}")

    total_price += item_price * item_quantity
    # 9. Create space strings


    # 10. Print the item name, price, and quantity


# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
total_cost = sum(item["Price"]*item["Quantity"] for item in order_list)
print(f"\nTotal cost : ${total_cost:.2f}")
print("Arigatogozaimasu! Thanks for dining with us!")