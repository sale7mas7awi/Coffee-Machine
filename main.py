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
money = 0.0

def calculate_money(quarters, dimes, nickels, pennies):
    total_money  = quarters * 0.25 + dimes *0.10 + nickels * 0.05 + pennies * 0.01
    return total_money



def insert_coins():
    print("Please insert coins.")
    quarters=input("How many quarters?:")
    dimes=input("How many dimes?:")
    nickels=input("How many nickels?:")
    pennies=input("How many pennies?:")
    total_money = calculate_money(int(quarters), int(dimes), int(nickels), int(pennies))
    return total_money


turn_on = True
while turn_on:

    user_answer = input("What would you like? (espresso/latte/cappuccino):").lower()

    if user_answer == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money:.2f}")


    elif user_answer in MENU:
        if user_answer == "espresso":
            if resources["water"]<50:
                print("Sorry there is not enough water.")
            elif resources["coffee"]<18:
                print("Sorry there is not enough coffee.")
            elif resources["water"]>=50 and resources["coffee"]>=18:
                inserted=insert_coins()
                if inserted>=1.5:
                    resources["water"] -= 50
                    resources["coffee"] -= 18
                    money += 1.5
                    change =round( inserted - 1.5,2)
                    print(f"Here is ${change:.2f} in change.")
                    print("Here is your espresso ☕. Enjoy!")
                elif inserted<1.5:
                    print("Sorry that's not enough money. Money refunded.")



        if user_answer == "latte":
            if resources["water"]<200:
                print("Sorry there is not enough water.")
            elif resources["coffee"]<24:
                print("Sorry there is not enough coffee.")
            elif resources["milk"]<150:
                print("Sorry there is not enough milk.")
            elif resources["water"]>=200 and resources["coffee"]>=24 and resources["milk"]>=150:
                inserted=insert_coins()
                if inserted>=2.50:
                    resources["water"] -= 200
                    resources["coffee"] -= 24
                    resources["milk"]-=150 
                    money += 2.50
                    change = round(inserted - 2.50,2)
                    print(f"Here is ${change:.2f} in change.")
                    print("Here is your latte ☕. Enjoy!")
                elif inserted<2.50:
                    print("Sorry that's not enough money. Money refunded.")



        if user_answer == "cappuccino":
            if resources["water"]<250:
                print("Sorry there is not enough water.")
            elif resources["coffee"]<24:
                print("Sorry there is not enough coffee.")
            elif resources["milk"]<100:
                print("Sorry there is not enough milk.")
            elif resources["water"]>=250 and resources["coffee"]>=24 and resources["milk"]>=100:
                inserted=insert_coins()
                if inserted>=3.00:
                    resources["water"] -= 250
                    resources["coffee"] -= 24
                    resources["milk"]-=100
                    money += 3.00
                    change = round(inserted - 3.00,2)
                    print(f"Here is ${change:.2f} in change.")
                    print("Here is your cappuccino ☕. Enjoy!")

                    
    elif user_answer == "off":
        print("Turning off the coffee machine.")
        turn_on = False

