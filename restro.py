print("Welcome to our restaurant!")

# Define the menu as a dictionary
menu = {
    "pizza": 40,
    "pasta": 50,
    "burger": 60,
    "salad": 70,
    "coffee": 80
}

# Display the menu
for item, price in menu.items():
    print(f"{item}: R${price}")

order_total = 0

item_1 = input("Enter the first item you want to order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"{item_1} added to your order. Current total: R${order_total}")
else:
    print(f"Sorry, {item_1} is not on the menu.")

item_2 = input("Enter the second item you want to order: ")
if item_2 in menu:
    order_total += menu[item_2]
    print(f"{item_2} added to your order. Current total: R${order_total}")
else:
    print(f"Sorry, {item_2} is not on the menu.")

print(f"Your final order total is: R${order_total}")
