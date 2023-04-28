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
    "water": 500,
    "milk": 300,
    "coffee": 200,
    "money": 0,
}

coin = ["Quarters", "Dimes", "Nickles", "Pennies"]


def enough_resource(required):
    for i in required:
        if required[i] > resources[i]:
            print(f"Sorry, there is not enough {i}!")
            return False
    return True


def reduce_resources(resource, amount):
    resources[resource] -= amount


def process_coins(coffee_type):
    total_coins = 0

    for i in range(4):
        coin_input = int(input(f"Insert {coin[i]}\n"))
        if i == 0:
            coin_input *= 0.25
            total_coins += coin_input
        elif i == 1:
            coin_input *= 0.1
            total_coins += coin_input
        elif i == 2:
            coin_input *= 0.05
            total_coins += coin_input
        elif i == 3:
            coin_input *= 0.01
            total_coins += coin_input
    change = total_coins - MENU[coffee_type]['cost']
    if total_coins < MENU[coffee_type]['cost']:
        print("Sorry, that's not enough money. Money refunded")
        print(total_coins)
    elif total_coins >= MENU[coffee_type]['cost']:
        resources["money"] += MENU[coffee_type]['cost']

        reduce_resources("water", MENU[coffee_type]["ingredients"]["water"])
        reduce_resources("coffee", MENU[coffee_type]["ingredients"]["coffee"])
        if coffee_type == "espresso":
            True
        else:
            reduce_resources("milk", MENU[coffee_type]["ingredients"]["milk"])
        if change > 0:
            print(f"Here is ${round(change, 2)} dollars in change.")

        print(f"Here is your {coffee_type}. Enjoy!")


if __name__ == "__main__":
    while True:
        user_input = input("What would you like?\n").lower()

        if user_input == "off":
            break
        elif user_input == "report":
            print(
                f"Water: {resources['water']}\n"
                f"Milk: {resources['milk']}\n"
                f"Coffee: {resources['coffee']}\n"
                f"Money: {resources['money']}"
            )
        else:
            drink = MENU[user_input]
            if enough_resource(drink["ingredients"]):
                process_coins(user_input)




