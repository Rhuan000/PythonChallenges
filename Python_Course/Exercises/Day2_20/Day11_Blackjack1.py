import random


user_cards = []
computer_cards = []
is_game_over = False
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card



def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Its a Drawn"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Oponent went over. you win"
    elif user_score > computer_score:
        return "you win"
    else:
        return "you lose"
for n in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f'your cards: {user_cards}, current score: {user_score} ')
    print(f'the first card of computer is: {computer_cards[0]}')
    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_answer = input('wanna add another card? "y" or "n"')
        if user_answer == 'y':
            user_cards.append(deal_card())
        else:
            is_game_over = True

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

print(f'your final hand is {user_cards} and the score is: {user_score}')
print(f'the computer final hand is {computer_cards}, and final score is: {computer_score}')
print(compare(user_score,computer_score))