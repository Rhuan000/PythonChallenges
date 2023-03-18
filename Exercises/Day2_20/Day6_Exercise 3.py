def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():

while at_goal() != True:

    if right_is_clear(): # não precisa colocar == true se não o loop nunca irá acabar
        turn_right()
    if wall_in_front():
        turn_left()

    if front_is_clear():
        move()

