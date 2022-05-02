import turtle

#Importing screen and objects on the screen
from screen import *
from player import *
from obstacles import *

#Importing the functions to make the game run within the Game Loop
from obstacle_attributes import move_right, move_left, move_up, move_down, obstacle_border, collision
from player_border_check import player_border_check


#Level_1 Game Loop
def level1(death_count, death_label, level_number):
    borders()
    break_condition = True
    while break_condition:
        wn.update()

        #These functions move the obstacles
        move_right(obstacle_list[0:12:2])
        move_left(obstacle_list[1:12:2])
        move_up(obstacle_list[12:27:2])
        move_down(obstacle_list[13:27:2])

        #These functions keep the player and obstacles within a defined boundary
        obstacle_border(obstacle_list)
        player_border_check(player)

        #This function iterates through all level 1 obstacles and makes collisions between player and obstacles
        for i in obstacle_list:
            death_count = collision(i, player, death_count, death_label, level_number)

        #This function defines a player winning and breaks the loop moving them to the next level
        if player.xcor() > (winning_square.xcor() - 20):
            level_number += 1
            for i in obstacle_list:
                i.hideturtle()
            break_condition = False
    return death_count, level_number
