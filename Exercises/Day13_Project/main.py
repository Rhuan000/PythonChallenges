import random
import art
from game_data import data

#High lower game, this game will ask the player who has more followers

def choice():
    '''Get a random Ask for user'''
    choice = random.choice(data)
    data.remove(choice)
    return choice

def comparing(first_choice,second_choice) -> bool:
    '''If the firs option has most followers than second will return True.'''
    number_of_follower = first_choice['follower_count']
    number_of_follower2 = second_choice['follower_count']
    if number_of_follower > number_of_follower2:
        return True
    else:
        return False

def format(choice):
    '''Format the Output'''
    return (f"compare A: {choice['name']}, a {choice['description']}, from {choice['country']} ")

def main():
    should_run = True
    score = 0
    #Main Loop to Run the game.
    print(art.logo)
    while should_run:
        #Getting two questions for player
        choice1 = choice()
        choice2 = choice()

        print('who has more followers in instagram?')
        print(f"compare A: {choice1['name']}, a {choice1['description']}, from {choice1['country']} ")
        print(art.vs)
        print(f"Against B: {choice2['name']}, a {choice2['description']}, from {choice2['country']} ")

        #Getting the answer of the user.
        user_answer = input('Type "A" or "B" ').upper()
        #checking if the answer is the right choice, if not the right answer, should return the score and ask if the user want to continuous play
        if user_answer == 'A':
            if comparing(choice1, choice2) == True:
                score += 1
            else:
                print(f'You lose! {score} this is your final score.')
                if input('Wanna continue? "yes" or "no" ') == 'no':
                    should_run = False
                else:
                    score = 0
        elif user_answer == 'B':
            if comparing(choice1, choice2) == False:
                score += 1
            else:
                print(f'You lose! {score} this is your final score.')
                if input('Wanna continue? "yes" or "no" ') == 'no':
                    should_run = False
                else:
                    score = 0

#callig the Main function
main()