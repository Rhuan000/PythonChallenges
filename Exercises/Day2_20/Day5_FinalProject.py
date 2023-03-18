import random

letters = ['a ', 'b ', 'c ', 'd ', 'e ', 'f ', 'g ', 'h ', 'i ', 'j ', 'k ', 'l ', 'm ', 'n ', 'o ', 'p ', 'q ', 'r ', 's ', 't ', 'u ', 'v ', 'w ', 'x ', 'y ', 'z ', 'A ', 'B ', 'C ', 'D ', 'E ', 'F ', 'G ', 'H ', 'I ', 'J ', 'K ', 'L ', 'M ', 'N ', 'O ', 'P ', 'Q ', 'R ', 'S ', 'T ', 'U ', 'V ', 'W ', 'X ', 'Y ', 'Z ']
symbols = ['{ ','} ','( ',') ','[ ','] ','. ',', ',': ','; ','+ ','- ','* ','/ ','& ','| ','< ','> ','= ','~ ']
numbers = ['0 ','1 ','2 ','3 ','4 ','5 ','6 ','7 ','8 ','9 ']

How_many_letters = int(input('How many letters would you like in your password?'))
How_many_symbols = int(input('How many symbols would you like in your password?'))
How_many_numbers = int(input('How many numbers would you like in your password?'))

#variáveis com string vazia para serem preenchidas aleatóriamente na soma das strings.
final_password = ''
random_numbers_total = ''
random_letters_total = ''
random_symbols_total = ''

#gerar uma string aleatória com a quantidade de letras pedidos na senha
for letters_in_password in range(0, How_many_letters):
    random_letters = random.choice(letters)
    random_letters_total = random_letters_total + random_letters
#gerar uma string aleatória com a quantidade de simbolos pedidos na senha
for symbols_in_password in range(0, How_many_symbols):
    random_symbols = random.choice(symbols)
    random_symbols_total = random_symbols_total + random_symbols

#gerar uma string aleatória com a quantidade de numeros pedidos na senha
for numbers_in_password in range(0, How_many_numbers):
    random_numbers = random.choice(numbers)
    random_numbers_total = random_numbers_total + random_numbers
#separar a string e colocar como lista. e embaralhar a lista
full_caracters = (random_numbers_total + random_letters_total + random_symbols_total).split()
random.shuffle(full_caracters)
#somar a lista com as strings e formar uma nova e ultima string com a senha.
for final_list in full_caracters:
    final_password = final_password + final_list

print(f'A sua nova senha será: {final_password}')


'''#Password Generator Project right way:
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")







'''