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


def check_enough_resource(resource, required):
    if resources[resource] < required:
        print(f"Sorry, there is not enough {resource}")
        return False
    else:
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
        match user_input:
            case "off":
                break
            case "report":
                print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: {resources['money']}")
            case "espresso":
                if check_enough_resource("water", 50) and check_enough_resource("coffee", 18):
                    process_coins("espresso")
            case "latte":
                if check_enough_resource("water", 200) and check_enough_resource("coffee", 150) and check_enough_resource("milk", 24):
                    process_coins("latte")
            case "cappuccino":
                if check_enough_resource("water", 250) and check_enough_resource("coffee", 100) and check_enough_resource("milk", 24):
                    process_coins("cappuccino")




