myInput = input("Input a number: ")
if '.' in myInput:
    try:
        myInput = float(myInput)
        print(f'{myInput} is a float')
    except ValueError:
        print(f'{myInput} is not a number')
else:
    try:
        myInput = int(myInput)
        print(f'{myInput} is an integer')
    except ValueError:
        print(f'{myInput} is not a number')

guess = input('teste')
if '' in guess:
    try:
        guess = int(guess)

    except ValueError:
        print(f'{guess}its not a number')

