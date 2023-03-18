#Scope

#local scope:

def drink_potion():
    potion_strenght = 2
    print(potion_strenght)
#print(potion_strenght)  how can we see, we gonna find a error.


#global scope
player_health = 10
def drink_potion2():
    potion_strenght = 2
    print(player_health)
drink_potion2()
print(player_health)

#this concept work with almost everything
def game():
    def drink_potion3():
        potion_strenght = 2
    drink_potion3()

#there is no block scope

game_level = 3
enemies = ['skeleton', 'zombie', 'alien']
if game_level < 5:
    new_enemy = enemies[0]
print(new_enemy)

#Modifying Global Scope
enemies = 1
def increase_enemies():
    global enemies # i'm especifying this variable its a global variable. defined somewhere outside the function
    enemies += 1
    print(f'{enemies}')
print(enemies)

#and the another way its return.

def increase_enemies2():
    return enemies + 1
enemies = increase_enemies()
print(enemies)

#global constancy
PI = 3.14159 #we create a variable with upper letters