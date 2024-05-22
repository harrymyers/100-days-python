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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(oder_ingredients):
    for item in oder_ingredients:
        if oder_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def insert_coins():
    print("Insert Coins")
    quarters = int(input("Quarters"))
    dimes = int(input("Dimes"))
    nickels = int(input("Nickels"))
    pennies = int(input("Pennies"))
    total = .01 * pennies + .05 * nickels + .1 * dimes + .25 * quarters
    return total


def is_transaction_successful(total, cost):
    if total < cost:
        print("Sorry that's not enough, money refunded")
        return False
    print(f"change: ${round(total - cost, 2)}")
    global profit
    profit += cost
    return True


def make_coffee(name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {name}")


is_on = True
profit = 0

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            t = insert_coins()
            if is_transaction_successful(t, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
