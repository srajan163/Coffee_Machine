MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

Resorces = {
    "water": 300,
    "milk": 200,
    "coffee": 100

}


def is_sufficent_ingrident(order_ingrident):
    """Return True  when order is made ,False ingredient is insufficent"""
    for item  in order_ingrident:
        if order_ingrident[item] >=Resorces[item]:

            print(f"sorry We don't have enough {item}")
            return False
    return True
def process_coin():
    """Return The total Calculated From the coin """
    print("insert Coin")
    total=int(input("How many quarters"))*0.25
    total+=int(input("How many dimes"))*0.1
    total += int(input("How many nickles ")) * 0.05
    total += int(input("How many pennies")) * 0.01
    return total
def is_transaction_successful(money_recived,drink_cost):
    """To Check The Transaction is Successfully or Not"""
    if money_recived>=drink_cost:
        change=round(money_recived-drink_cost,2)
        print(f"Here is ${change} left ")
        global profit
        profit+=drink_cost
        return True
    else:
        print("insufficient Balance,refund money")
        return False
def make_coffee(drink_name,order_ingredients):
    for items in order_ingredients:
        Resorces[items]-=order_ingredients[items]
    print(f"Here is your {drink_name} ")

is_on=True
while is_on:
    choice = input("What would you like? (espresso,latte,cappucciono) :")
    if choice == "off":
        is_on = False
    elif choice == "report":

        print(f"Water: {Resorces['water']}ml")
        print(f"Milk: {Resorces['milk']}ml")
        print(f"Coffe: {Resorces['coffe']}g")
        print(f"Money  ${profit}")
    else:
        drink = MENU[choice]
        if is_sufficent_ingrident(drink["ingredients"]):
            payment=process_coin()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])