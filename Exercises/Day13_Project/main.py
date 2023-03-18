import random

import art
from game_data import data


def choice():
    choice = random.choice(data)
    data.remove(choice)
    return choice
choice1 = choice()
choice2 = choice()
def comparing(first_choice,second_choice):
    number_of_follower = first_choice['follower_count']
    number_of_follower2 = second_choice['follower_count']
    if number_of_follower > number_of_follower2:
        return True
    else:
        return False
def format(choice):
    return (f"compara A: {choice['name']}, a {choice['description']}, from {choice['country']} ")
def main(choice1,choice2):
    should_run = True
    score = 0
    while should_run:
        choice3 = choice()
        choice1 = choice2
        choice2 = choice3
        print(art.logo)
        print('who has more followers in instagram?')
        print(f"compara A: {choice1['name']}, a {choice1['description']}, from {choice1['country']} ")
        print(art.vs)
        print(f"Against B: {choice2['name']}, a {choice2['description']}, from {choice2['country']} ")
        user_answer = input('Type "A" or "B" ').upper()
        if user_answer == 'A':
            if comparing(choice1, choice2) == True:
                score += 1
            else:
                print(f'You lose!{score} this is your final score.')
                if input('Wanna continue? "yes" or "no" ') == 'no':
                    should_run = False
                else:
                    score = 0
        elif user_answer == 'B':
            if comparing(choice1, choice2) == False:
                score += 1
            else:
                print(f'You lose! {score} this is your final score.')
                if input('Wanna continue? "yes" or "no"') == 'no':
                    should_run = False
                else:
                    score = 0
main(choice1,choice2)