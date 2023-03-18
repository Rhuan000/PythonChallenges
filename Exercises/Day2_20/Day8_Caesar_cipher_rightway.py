def encrypt(plain_text, shift_amount, direction):
    cypher_text = ''
    shift_amount *= -1
    for char in plain_text:

        if char in alphabet:
            position = alphabet.index(char)
            if direction == 'encode':
                new_position = position + shift_amount
            elif direction == 'decode':

                new_position = position - shift_amount
            new_letter = alphabet[new_position]
            cypher_text += new_letter
        else:
            cypher_text += char
    print(cypher_text)

should_continue = True

while should_continue:

    alphabet = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h','i','j','k','l','m','n','o','p', 'q','r','s','t','u','v','w', 'x', 'y', 'z', 'a','b', 'c', 'd', 'e', 'f', 'g', 'h','i','j','k','l','m','n','o','p', 'q','r','s','t','u','v','w', 'x', 'y', 'z']
    direction = input('Type "encode" to encrypt, type "decode" to decrypt:\n')
    text = input('Type your message: \n').lower()
    shift = int(input('Type the shift number:\n'))
    shift = shift % 26
    encrypt(text, shift, direction)
    result = input('do you wanna continue?\n')
    if result == 'no':
        should_continue = False
