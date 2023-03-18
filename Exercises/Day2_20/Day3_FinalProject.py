print('Welcome to Treasure island. Your mission is to find the treasure.')
left_or_right = input('left or right?').lower()

if left_or_right == 'right':
    print('game over')
elif left_or_right == 'left':
    swim_wait = input('swim or wait?').lower()
    if swim_wait == 'swim':
        print('Game over')
    elif swim_wait == 'wait':
        which_door = input('which door?, blue,red or yellow?')
        if which_door == 'yellow':
            print('you won')
        else:
            print('you lose')

