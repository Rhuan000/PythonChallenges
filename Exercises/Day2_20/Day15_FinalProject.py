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
user_coin = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def set_coin(user_coin,user_answer):
    if user_coin < MENU[user_answer]['cost']:
        user_coin = float(input('coin insuficient, set coin: '))
        return user_coin


def check_resources(resources):
    for key in resources:
        if resources[key] < 0:
            resources[key] = 0
            return f'Sorry {key} is insuficient'
    else:
        return False

def espresso(MENU,resources,user_coin):
    water = MENU['espresso']['ingredients']['water']
    coffee = MENU['espresso']['ingredients']['coffee']
    cost = MENU['espresso']['cost']
    resources['water'] -= water
    resources['coffee'] -= coffee
    user_coin -= cost
    return resources, user_coin
def latte(MENU,resources,user_coin):
    water = MENU['latte']['ingredients']['water']
    coffee = MENU['latte']['ingredients']['coffee']
    milk = MENU['latte']['ingredients']['milk']
    cost = MENU['latte']['cost']
    resources['water'] -= water
    resources['coffee'] -= coffee
    resources['milk'] -= milk
    user_coin -= cost
    return resources, user_coin
def cappuccino(MENU,resources,user_coin):
    water = MENU['cappuccino']['ingredients']['water']
    coffee = MENU['cappuccino']['ingredients']['coffee']
    milk = MENU['cappuccino']['ingredients']['milk']
    cost = MENU['cappuccino']['cost']
    resources['water'] -= water
    resources['coffee'] -= coffee
    resources['milk'] -= milk
    user_coin -= cost
    return resources, user_coin

check_recourses = check_resources(resources)
user_answer = 'on'
while user_answer != 'off':
    user_answer = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_answer == 'espresso':
        espresso(MENU, resources, user_coin)
        check_recourses = check_resources(resources)
        if check_recourses == False:
            print(f'enjoy your{user_answer}!')
        else:
            print(check_recourses)
    elif user_answer == 'latte':
        latte(MENU,resources,user_coin)
        check_recourses = check_resources(resources)
        if check_recourses == False:
            print(f'enjoy your {user_answer}')
        else:
            print(check_recourses)
    elif user_answer == 'cappuccino':
        cappuccino(MENU,resources,user_coin)
        check_recourses = check_resources(resources)
        if check_recourses == False:
            print(f'enjoy your {user_answer}')
        else:
            print(check_recourses)
    elif user_answer == 'report':
        for key in resources:
            print(key,resources[key])
