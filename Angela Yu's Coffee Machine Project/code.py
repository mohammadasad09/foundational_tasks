
initial_ingredients = {'water': 300, 'milk': 200, 'coffee': 100, 'money': 0}
espresso_recipe = {'water': 50, 'coffee': 18, 'milk': 0, 'money': 1.5}
latte_recipe = {'water': 200, 'coffee': 24, 'milk': 24, 'money': 2.5}
cappuccino_recipe = {'water': 250, 'coffee': 24, 'milk': 100, 'money': 3}


user_balance = 0

def drink_assignment(customer_drink):
    if customer_drink == '1':
        return espresso_recipe
    elif customer_drink == '2':
        return latte_recipe
    elif customer_drink == '3':
        return cappuccino_recipe
    else:
        print("Invalid choice. Please enter a valid number for a drink option. Choose from (1,2,3): ")
        return None

def resource_deduction(customer_drink):
    out_of_budget = False
    for ingredient in ['water', 'coffee', 'milk']: 
        if customer_drink[ingredient] > initial_ingredients[ingredient]:
            print(f"Sorry, we are out of {ingredient}. Please choose another option or check the available resources.")
            out_of_budget = True
            break
    if not out_of_budget:
        initial_ingredients['water'] -= customer_drink['water']
        initial_ingredients['coffee'] -= customer_drink['coffee']
        initial_ingredients['milk'] -= customer_drink['milk']
        print(f"Amount of water left: {initial_ingredients['water']} ml")
        print(f"Amount of coffee left: {initial_ingredients['coffee']} g")
        print(f"Amount of milk left: {initial_ingredients['milk']} ml")
        return True
    else:
        return False

def add_money_to_balance(pennies, nickels, dimes, quarters):
    total_pennies = pennies * 0.01
    total_nickels = nickels * 0.05
    total_dimes = dimes * 0.10
    total_quarters = quarters * 0.25
    total_money = total_pennies + total_nickels + total_dimes + total_quarters
    global user_balance
    user_balance += total_money
    initial_ingredients['money'] += total_money
    return total_money

def receipt():
    print("\nReceipt:")
    print(f"Water remaining: {initial_ingredients['water']} ml")
    print(f"Milk remaining: {initial_ingredients['milk']} ml")
    print(f"Coffee remaining: {initial_ingredients['coffee']} g")
    print(f"Money in the machine: ${round(initial_ingredients['money'], 2)}\n")

while True:
    user_choice = input("\nWhat would you like to have today? Please choose from the following options:\n"
                        "1. Espresso\n2. Latte\n3. Cappuccino\n"
                        "(You can also type 'receipt' to check the remaining resources, or type 'exit' to quit)\n")
    
    if user_choice.lower() == 'exit':
        print(f"Thank you for using the coffee machine! You are leaving with a change of ${round(user_balance, 2)}. Have a great day!")
        break
    
    if user_choice.lower() == 'receipt':
        receipt()
        continue

    customer_drink = drink_assignment(user_choice)

    if customer_drink:
        if user_balance < customer_drink['money']:
            print(f"You need at least ${customer_drink['money']} for this drink, but your current balance is ${round(user_balance, 2)}.")
            number_of_pennies = int(input("Please enter the number of pennies you are adding: "))
            number_of_nickels = int(input("Please enter the number of nickels you are adding: "))
            number_of_dimes = int(input("Please enter the number of dimes you are adding: "))
            number_of_quarters = int(input("Please enter the number of quarters you are adding: "))
            
            add_money_to_balance(number_of_pennies, number_of_nickels, number_of_dimes, number_of_quarters)
            print(f"Your new balance is: ${round(user_balance, 2)}")
        
        if user_balance >= customer_drink['money']:
            user_balance -= customer_drink['money']
            initial_ingredients['money'] -= customer_drink['money']
            
            if resource_deduction(customer_drink):
                print("Enjoy your coffee!\n")
            else:
                print("Sorry, we can't make your drink due to insufficient resources. Please try again or choose another option.\n")
        else:
            print("You still don't have enough money. Please add more or select a different option.")
    else:
        print("Please select a valid drink option from the menu.\n")
