from art import CUP
from dicts import MENU, COIN_VALUES, machine_resources

def print_art():
    """Prints coffee cup"""
    print(CUP)

def prompt_user():
    """Prompts the user for what beverage they would like."""
    return input("What would you like? (espresso/latte/cappuccino): ")

def print_report(resources):
    """
    Prints a report of the current resources in the coffee machine.

    Args:
        resources (dict): A dictionary containing the current resources in the coffee machine.

    Returns:
        None
    """
    print(f"\nWater:  {resources["water"]}ml")
    print(f"Milk:   {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money:  ${resources["money"]}")

def check_resources(res_current, res_request):
    """
    Checks there are enough resources available to perform an operation.

    Parameters:
    res_current (dict): The resources currently available in the machine.
    res_request (dict): The resources required for the operation.

    Returns:
    bool: True if there are enough resources, False otherwise.
    """
    if "milk" in res_request.keys():
        milk = res_request["milk"] <= res_current["milk"]
    else:
        milk = True
    water = res_request["water"] <= res_current["water"]
    coffee = res_request["coffee"] <= res_current["coffee"]
    if milk and water and coffee:
        return True
    return False

def process_coins(req_amount):
    """
    Process the coins provided by the user and calculate the change.

    Args:
        req_amount (float): The required amount for the transaction.

    Returns:
        tuple: A tuple containing the change amount (float) and a boolean indicating if there is enough money.
    """
    total = 0.0
    change = 0.0

    total += float(input("Insert the number of Quarters you have: ")) * COIN_VALUES["quarter"]
    total += float(input("Insert the number of Dimes you have: ")) * COIN_VALUES["dime"]
    total += float(input("Insert the number of Nickles you have: ")) * COIN_VALUES["nickle"]
    total += float(input("Insert the number of Pennies you have: ")) * COIN_VALUES["pennie"]

    if total < req_amount:
        enough_money = False
        return change, enough_money
    else:
        change = total - req_amount
        enough_money = True
        return change, enough_money

machine_on = True

while machine_on:
    print_art()
    user_input = prompt_user() 
    if user_input in MENU.keys():
        req_coins = MENU[user_input]["cost"] 
        req_ingredients = MENU[user_input]["ingredients"] 
        change, enough_money = process_coins(req_coins) 
        if enough_money and check_resources(machine_resources, req_ingredients):
            if "milk" in req_ingredients.keys():
                machine_resources["milk"] -= req_ingredients["milk"]
            machine_resources["coffee"] -= req_ingredients["coffee"]
            machine_resources["water"] -= req_ingredients["water"]
            machine_resources["money"] += req_coins
            if change > 0:
                print(f"Here is your change: ${change}")
            print(f"Thanks for ordering a {user_input}, we hope you enjoy it!")
        elif not check_resources(machine_resources, req_ingredients):
            print("Sorry, the machine is out of resources to make your coffee....")
        elif not enough_money:
            print("Sorry, you didn't put enough coins into the machine...")
    elif user_input == "off":
        machine_on = False
        print("The coffee machine has been switched off. GOOD BYE!")
    elif user_input == "report":
        print_report(machine_resources)
    else:
        print("You didn't select a valid option...")
