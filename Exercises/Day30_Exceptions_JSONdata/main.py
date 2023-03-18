'''try:
    file = open('a_file.txt')
    a_dictionary = {"key":"value"}
except FileNotFoundError:
    file = open('a_file.txt', 'w')
    file.write('something')
except KeyError as error_message:
    print(f'the key: {error_message}, does not exist')
else:
    print(file.read())
finally:
    file.close()'''

height = int(input('Height: '))
weight = int(input('weight: '))

if height > 3:
    raise ValueError('human height should not be over 3 meters')


bmi = weight / height ** 2