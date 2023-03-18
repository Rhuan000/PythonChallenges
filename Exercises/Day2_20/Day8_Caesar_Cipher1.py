def encrypt(text1, shift1):
    crypt = []
    position = 0
    Final_phrase = ''
    end = False
# for letter in alphabet



    while not end:
        contagem = 0
        for check_alphabet in alphabet:
            if contagem == 21:
                contagem = 0
            elif position >= len(text1):
                end = True
            elif check_alphabet == text1[position]:
                crypt.append(alphabet[contagem + shift1])
                position += 1
            contagem += 1
    for soma in crypt:
        Final_phrase += soma
    print(Final_phrase)

def decrypt(text2,shift2):
    decryp = []
    position = 0
    Final_phrase = ''
    end = False
    while not end:
        contagem = 0
        for check_alphabet in alphabet:
            if contagem == 4:
                contagem = 25
            elif position >= len(text2):
                end = True
            elif check_alphabet == text2[position]:
                decryp.append(alphabet[contagem - shift2])
                position += 1
            contagem += 1
    for soma in decryp:
        Final_phrase += soma
    print(Final_phrase)





alphabet = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h','i','j','k','l','m','n','o','p', 'q','r','s','t','u','v','w', 'x', 'y', 'z']
direction = input('Type "encode" to encrypt, type "decode" to decrypt:\n')
text = input('Type your message: \n').lower()
shift = int(input('Type the shift number:\n'))

if direction == 'encode':
    encrypt(text, shift)
elif direction == 'decode':
    decrypt(text, shift)



