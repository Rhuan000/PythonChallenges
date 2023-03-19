print('Welcome to the rollercoaster!')
height = int(input('what is your height in cm?'))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input('What is your age?'))
    if age < 12:
        bill += 5
        print(f'tickets are: {bill}$')

    elif age <= 18:
        bill += 7
        print(f'tickets are: {bill}$')

    if age >= 45 or age <= 55:
        bill = 0

    else:
        bill += 12
        print(f'tickets are: {bill}$')
    wants_photo = str(input('Do you want a photo taken? Y or N.'))
    if wants_photo == 'Y':
        bill += 3
        print(f'total bill is {bill}$')
    print(f'you total bill is {bill}$')
    if age >= 45 or age <= 55:
        bill = 0
else:
    print('sorry, you have to grow taller before you can ride')