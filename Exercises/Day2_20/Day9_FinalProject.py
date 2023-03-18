import os

print('Welcome to the secret auction program')

all_participants_data = {}
winner_data = {}
reserve_key = ''
def add_in_dictionary():
    end = False
    while end == False:
        name = input('What is your name?\n')
        bid = int(input('What is your bid?: $'))
        all_participants_data[name] = bid
        answer = input('Are there any other bidders? type "yes" or "no"')
        if answer == 'no':
            end = True
        else:
            os.system('clear')
    print(all_participants_data)
def bid_check():
    highest_bid = 0
    for key in all_participants_data:
        score = all_participants_data[key]
        if score > highest_bid:
            highest_bid = score
            reserve_key = key
    winner_data[reserve_key] = highest_bid

    print(winner_data)



def main():
    add_in_dictionary()
    bid_check()
main()

