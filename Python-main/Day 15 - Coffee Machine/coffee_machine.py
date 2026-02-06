from asyncio import constants
import coffee_data


def main():
    
    is_on = True

    # Copy the starting resource from coffee_data
    machine_resource = coffee_data.resources

    # Add a new resource 'money' to the dict
    machine_resource['money'] = 0

    # loop while the machine is turned on
    while is_on:
        decision = 0

        # Loop while the input decision is not "Off"
        while not decision == 5:
            decision = int(input(f'''
            What would you like?
            [1]Expresso 
            [2]Latte 
            [3]Cappuccino
            [4]Report
            [5]Off
            Enter a choice : '''))

            # only run make_coffee function if check_resource function returns true which means there is enough
            # resources
            if decision == 1:
                if check_resource("espresso", machine_resource) :
                    make_coffee("espresso", machine_resource)           
            elif decision == 2:
                if check_resource("latte", machine_resource)  :
                    make_coffee("latte", machine_resource)               
            elif decision == 3:   
                if check_resource("cappuccino", machine_resource)  :
                    make_coffee("cappuccino", machine_resource)          
            elif decision == 4:
                print_report(machine_resource)              
            elif decision == 5:
                is_on = False               
            else:
                continue

def insert_coins(cost):
    '''
        Prompt user to insert coins
        Calculate the total value of the total coins inserted
        Return True if the value of total coins is greater than the cost of the coffee
        Return False if the value of total coins is lesser than the cost of the coffee
    '''
    QUARTERS = 0.25
    DIMES = 0.10
    NICKLES = 0.05
    PENNIES = 0.01

    print(f"Cost of coffee is $ {'{:.2f}'.format(cost)}... Please Insert coins....")
    quarters = int(input("How many quarters? : "))
    dimes = int(input("How many dimes? : "))
    nickles = int(input("How many nickles? : "))
    pennies = int(input("How many pennies? : "))

    coins_total = (quarters * QUARTERS) + (dimes * DIMES) + (nickles * NICKLES) + (pennies * PENNIES)
    if coins_total > cost:
        coins_change = coins_total - cost
        # '{:.2f}'.format(coins_change) converts float to string with 2 decimal places
        print(f"Here is your change : $ {'{:.2f}'.format(coins_change)}")
        return True
    elif coins_total == cost:
        print("That is the exact amount.")
        return True
    else:
        print("The entered amount is not enough!! ")
        return False

def check_resource(coffee_name, resource):
    '''
        Check if resources are enough and print error message
        Return False if there is not enough ingridents 

        Runs the insert_coins function where it will return True if there is enough money and 
        False if the money inserted is not enough
    '''
    print(f"Checking resource for {coffee_name}")
    for ingrident, amount in coffee_data.MENU[coffee_name]["ingredients"].items():
        print(f"Required resource : {ingrident} > {amount}")
        if resource[ingrident] < amount:
            print(f"Not enough {ingrident}, please top up!!")
            pause()

            # exit when not enough resources
            return False

    # True if coins are enough and False if not enough

    return insert_coins(coffee_data.MENU[coffee_name]["cost"])
    


def make_coffee(coffee_name,resource):
    '''
        Initiate the process to make the coffee by minusing the ingridents from the resource pool
        Add the money that is paid for the coffee
        Print out the remaining resource available in the machine
    '''
    for ingrident, amount in coffee_data.MENU[coffee_name]["ingredients"].items():
        # Minus off the ingrident amount needed
        resource[ingrident] -= amount
    
    # Add the cost of the coffee to the machine
    resource["money"] += coffee_data.MENU[coffee_name]["cost"]

    # Print out the remaining resource in the machine
    # for ingrident, amount in resource.items():
    #     print(f"Resource avaiable : {ingrident} > {amount}")


def print_report(resource):
    '''
        Print the resources left on the machine
    '''
    print("-----------------------------------------------")
    print(f"Water   :   {resource['water']} ml")
    print(f"Milk    :   {resource['milk']} ml")
    print(f"Coffee  :   {resource['coffee']} g")
    print(f"Money   : $ {resource['money']}")
    print("-----------------------------------------------")
    pause()

def pause():
    '''
        Pause the program
    '''
    programPause = input("Press any key to continue.....")

if __name__ == "__main__":
    main()