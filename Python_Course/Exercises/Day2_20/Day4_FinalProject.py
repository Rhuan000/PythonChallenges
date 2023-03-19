import random





choose_player = int(input("What do you choose? Type 0 for Rock, 1 for Paper  or 2 for Scissors"))
choose_computer = random.randint(0,2)



rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
rps = [rock, paper,  scissors]
#essa foi a escolha do player
print(f'escolha do jogador:{choose_player}')
print(rps[choose_player])
#escolha do computador
print(f'Essa foi a escolha do computador:{choose_computer}')
print(rps[choose_computer])


if choose_player < 0 or choose_player > 2:
    print('invalid type, you lose')
elif choose_player == 0 and choose_computer == 2:
    print('you won')
elif choose_computer > choose_player:
    print('you lose')
elif choose_computer == 0 and choose_player == 2:
    print('You lose')
elif choose_player > choose_computer:
    print('You Won')
elif choose_computer == choose_player:
    print('its a Draw')





