for numeros in range(1,101):
    fizz = numeros % 3
    buzz = numeros % 5
    if buzz == 0 and fizz == 0:
        print('FizzBuzz')
    elif fizz == 0:
        print('Fizz')
    elif buzz == 0:
        print('Buzz')
    else:
        print(numeros)
