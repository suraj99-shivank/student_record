rent = float(input("Enter the rent amount: "))
food = float(input("Enter the food expenses: "))
electricity_spending = float(input("Enter the electricity spending: "))
charge_per_unit = float(input("Enter the charge per unit of electricity: "))
person = int(input("Enter the number of people sharing the expenses: "))
total_electricity_cost = electricity_spending * charge_per_unit
total_expenses = rent + food + total_electricity_cost
expense_per_person = total_expenses / person
print("each person should pay: ", expense_per_person)
