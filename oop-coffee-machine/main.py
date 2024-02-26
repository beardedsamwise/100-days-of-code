from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# The modules/classes that I've imported are not mine, these were provided by the course
# This code is mine though :)

power = True
coffee_machine = CoffeeMaker()
coffee_menu = Menu()
money_machine = MoneyMachine()

while power:
    print()
    selection = input(f"What beverage would you like? {coffee_menu.get_items()}: ")
    if selection == "report":
        coffee_machine.report()
    elif selection == "off":
        power = False
        print("Thank you for using a Python powered coffee machine! GOOD DAY!")
    elif selection in coffee_menu.get_items():
        drink = coffee_menu.find_drink(selection)
        if money_machine.make_payment(drink.cost):
            if coffee_machine.is_resource_sufficient(drink):
                coffee_machine.make_coffee(drink)
            else:
                print("Sadly there are not enough resources available in the machine to make your coffee...")
        else:
            print("You didn't insert enough coins...")
    else:
        print("You didn't select a valid option... Please try again...")