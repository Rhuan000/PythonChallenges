# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
division_test = year % 4

if division_test == 0:
    division_test2 = division_test % 100
    if division_test2 == 0:
        division_test3 = division_test2 % 400
        if division_test3 == 0:
            print('Leap year.')
        else:
            print('Not leap year.')
    else:
        print('Leap year.')
else:
    print('Not leap year.')


