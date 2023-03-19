import random

list_of_number = []

def computer_number(list_of_number):
    for number in range (0,101):
        list_of_number.append(number)
    computer_n = random.choice(list_of_number)
    return computer_n
chosen_number = computer_number(list_of_number)

def check_answer(life):
    guess = input(f'you have {life}, attempts remaining to guess the number.\n make a guess: ')
    if '' in guess:
        try:
            guess = int(guess)
            print(guess)
            return guess

        except ValueError:
            print('its not a number')
            guess = check_answer(life)
            return guess

def easy_game():
    life = 10
    print(chosen_number)
    while life != 0 and life != 11:
        check_answer1 = check_answer(life)
        if check_answer1 == chosen_number:
            print('you win!')
            life = 12
        elif check_answer1 > chosen_number:
            print('Too hight')
        elif check_answer1 < chosen_number:
            print('Too low')
        life -= 1
    if life == 0:
        print('You lose.')
def main():
    if input('choose a dificulty. Type "easy" or "hard": ') == 'easy':
        easy_game()




print('Welcome to the number guessing game!')
print("i'm thinking of a number between 1 and 100")

main()