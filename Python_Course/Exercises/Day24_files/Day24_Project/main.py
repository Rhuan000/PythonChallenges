with open('guests') as guest:
    guest_list = guest.readlines()

for guests in guest_list:
    with open('starting_letter', mode='r') as letter:
        guests = guests.strip()
        letter = letter.read()
        letter = letter.replace('name', guests)


    with open(f'./guests_email/{guests}', mode='w') as guests_letter:
        guests_letter.write(letter)


