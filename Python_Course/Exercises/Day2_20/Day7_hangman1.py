#Step 1
def make_display():
    for check_letters in chosen_word:
        display.append("_")
    print(display)

import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list =['staff','strength','strengths', 'stretch', 'stronghold', 'stymied', 'subway', 'swivel', 'syndrome', 'thriftless', 'thumbscrew', 'topaz', 'transcript', 'transgress', 'transplant', 'triphthong', 'twelfth', 'twelfths', 'unknown', 'unworthy', 'unzip', 'uptown', 'vaporize', 'vixen', 'vodka', 'voodoo', 'vortex', 'voyeurism', 'walkway', 'waltz', 'wave', 'wavy', 'waxy', 'wellspring', 'wheezy', 'whiskey', 'whizzing', 'whomever', 'wimpy', 'witchcraft', 'wizard', 'woozy', 'wristwatch', 'wyvern', 'xylophone', 'yachtsman', 'yippee', 'yoked', 'youthful', 'yummy', 'zephyr', 'zigzag', 'zigzagging', 'zilch', 'zipper',
'zodiac','zombie']
chosen_letters = []
display = []
chosen_word = random.choice(word_list)
endgame = False
round = 0
make_display()
total_life = 6
while not endgame:
    round +=  1
    letter_guess = input('choose a letter').lower()
    chosen_letters.append(letter_guess)
    contagem = 0
    for check_letters in chosen_word:

        if letter_guess == check_letters:
            display[contagem] = letter_guess
        contagem += 1
    if letter_guess not in display:
        total_life -= 1

    print(f'as letras escolhidas foram:{chosen_letters}, \n rodada {round}')
    print(stages[total_life])
    print(display)
    if total_life == 0:
        print('Você perdeu')
        print(f'a palavra era: {chosen_word}')
        endgame = True
    if '_' not in display:
        endgame = True
        print('Parabéns, você venceu!')
