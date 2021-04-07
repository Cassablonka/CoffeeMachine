from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True

while is_on:
    choice = input(f"Welcome to Cassa Coffee Roasters! What would you like to  have ? :  {menu.get_items()}")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        print(f'That would be ₹{drink.cost}')
        is_resources_sufficient = coffee_maker.is_resource_sufficient(drink)
        is_payment_successful = money_machine.make_payment(drink.cost)
        if is_resources_sufficient and is_payment_successful:
            coffee_maker.make_coffee(drink)