from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    is_on = True

    # Create a coffee machine as an object
    coffee_machine = CoffeeMaker()

    # Create a coffee menu as an object
    coffee_menu = Menu()

    # Create money_eater as an object
    money_eater = MoneyMachine()
    
    while is_on:
        user_choice = input(f"What would you like? ({coffee_menu.get_items()}) : ")

        # Check if the coffee entered by the user is in the menu
        # Stores the result in coffee_chosen variable
        coffee_chosen = coffee_menu.find_drink(user_choice)

        # If else loop to check the result
        if user_choice.lower() == "report":
            coffee_machine.report()
            money_eater.report()
        elif user_choice.lower() == "off":
            print("Machine turned off")
            is_on = False

        # if the find_drink method does not return None, means that the coffee is in the menu
        elif coffee_chosen is not None:
            
            # Check if the machine has enough resources for the chosen coffee
            # Will print out not enough messages if it is not sufficient
            if coffee_machine.is_resource_sufficient(coffee_chosen):
                money_eater.make_payment(coffee_chosen.cost)
                coffee_machine.make_coffee(coffee_chosen)

        # find_drinks method returns None, which means the drink is not in the menu
        else:
            continue
       
         

if __name__ == "__main__":
    main()