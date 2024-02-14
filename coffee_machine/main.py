# TODO: allow hidden operation of "off" to exit program
# TODO: Function: Process coins, if enough money presented store the money, offer change, if not return false

from art import CUP

def print_art():
    """Prints coffee cup"""
    print(CUP)

def prompt_user():
    """Prompts the user for what beverage they would like."""
    return input("What would you like? (espresso/latte/cappuccino): ")

def print_report(resources):
    """Prints a report of the current resources in the coffee machine."""
    print(f"Water:  {resources["water"]}ml")
    print(f"Milk:   {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money:  ${resources["money"]}")

def check_resources(res_current, res_request):
    """
    Checks there are enough resources available to perform an operation.
    res_current = the resources avaiable in the machine
    res_request = the resources we want to use
    """
    milk = res_request["milk"] <= res_current["milk"]
    water = res_request["water"] <= res_current["water"]
    coffee = res_request["coffee"] <= res_current["coffee"]
    if milk and water and coffee:
        return True
    return False

resources = {
    "water" : 300,
    "milk" : 50,
    "coffee" : 76,
    "money" : 2.5
}
print_art()
prompt_user()
print_report(resources)