from screen import starting_square

def move_right(x_list):
    """
    move_right iterates though a list and makes them move horiztonally to the right

    :param x_list: a list of objects that need to move
    """
    for i in x_list:
        i.setx(i.xcor() + i.dx)

def move_left(x_list):
    """
    move_left iterates though a list and makes them move horiztonally to the left

    :param x_list: a list of objects that need to move
    """
    for i in x_list:
        i.setx(i.xcor() - i.dx)

def move_up(y_list):
    """
    move_up iterates though a list and makes them move vertical

    :param y_list: a list of objects that need to move
    """
    for i in y_list:
        i.sety(i.ycor() + i.dy)

def move_down(y_list):
    """
    move_down iterates though a list and makes them move vertical

    :param y_list: a list of objects that need to move
    """
    for i in y_list:
        i.sety(i.ycor() - i.dy)

#Border check for obstacles
def obstacle_border(x_list):
    """
    obstacle_border takes in a list of objects and makes sure they don't go outside a certain boundary

    :x_list: a list of objects
    """
    for i in x_list:
        if i.xcor() < -390:
            i.setx(-390)
            i.dx *= -1
        if i.xcor() > 390:
            i.setx(390)
            i.dx *= -1
        if i.ycor() > 337.5:
            i.sety(337.5)
            i.dy *= -1
        if i.ycor() < -340:
            i.sety(-340)
            i.dy *= -1

#Collisions for Obstacles and Player
def collision(i, player, death_count, death_label, level_number, collision_height = 20, collision_width = 20):
    """
    collision takes the player and returns them to their starting spot when they run into an obstacle. It also adds 1 to the death count

    :i: An obstacle from the game
    :player: The player of the game
    :death_count: The variable that keeps track of death count
    :death_label: The label in the top left corner of the screen
    :level_number: The variable that keeps track of which level the user is on
    :collision_height: How far apart vertically the collision occurs from the centers of the player and i (the object)
    :collision_widtht: How far apart horiztonally the collision occurs from the centers of the player and i (the object)
    :return: Function returns the death count as to keep it updated properly
    """
    if (player.ycor() > i.ycor() - collision_height and player.ycor() < i.ycor() + collision_height) and (player.xcor() < i.xcor() + collision_width and player.xcor() > i.xcor() - collision_width):
        player.setx(starting_square.xcor())
        player.sety(starting_square.ycor())
        death_count += 1
        death_label.clear()
        death_label.write(f'Level {level_number}/3 | Deaths: {death_count}', align='center', font=("Courier", 24, "normal"))
    return death_count
