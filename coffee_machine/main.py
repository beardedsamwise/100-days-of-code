# TODO: process coffee order

from art import CUP

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
    milk = res_request["milk"] <= res_current["milk"]
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
    coins_provided = {
        "quarters": 0,
        "dimes": 0,
        "nickles": 0,
        "pennies": 0
    }

    coins_provided["quarters"] = input("Insert the number of Quarters you have: ")
    coins_provided["dimes"] = input("Insert the number of Dimes you have: ")
    coins_provided["nickles"] = input("Insert the number of Nickles you have: ")
    coins_provided["pennies"] = input("Insert the number of Pennies you have: ")
    total += coins_provided["quarters"] * COIN_VALUES["quarter"]
    total += coins_provided["dimes"] * COIN_VALUES["dime"]
    total += coins_provided["nickles"] * COIN_VALUES["nickle"]
    total += coins_provided["pennies"] * COIN_VALUES["pennie"]

    if total < req_amount:
        enough_money = False
        return change, enough_money
    else:
        change = total - req_amount
        enough_money = True
        return change, enough_money

COIN_VALUES = {
    "quarter" : 0.25,
    "dime" : 0.10,
    "nickle" : 0.05,
    "pennie" : 0.01
}

PRICES = {
    "espresso" : 2.0,
    "latte" : 2.5,
    "cappuccino" : 2.60
}

resources = {
    "water" : 300,
    "milk" : 50,
    "coffee" : 76,
    "money" : 2.5
}

machine_on = True

while machine_on:
    print_art()
    user_input = prompt_user() 
    if user_input in PRICES.keys():
        print("You ordered a coffee")
    elif user_input == "off":
        machine_on = False
        print("The coffee machine has been switched off. GOOD BYE!")
    elif user_input == "report":
        print_report(resources)
    else:
        print("You didn't select a valid option...")
