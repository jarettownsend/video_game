import turtle

#Importing screen and objects on the screen
from screen import *
from player import *
from obstacles_2 import *

#Importing the functions to make the game run within the Game Loop
from obstacle_attributes import move_up, move_down, obstacle_border, collision
from player_border_check import player_border_check

#Level_2 Game Loop
def level2(death_count, death_label, level_number):

    #Before the main loop this code resets the labels and the players
    death_label.clear()
    death_label.write(f'Level {level_number}/3 | Deaths: {death_count}', align='center', font=("Courier", 24, "normal"))
    player.setx(starting_square.xcor())
    player.sety(starting_square.ycor())
    break_condition = True

    #Main loop
    while break_condition:
        wn.update()

        #These functions move the obstacles
        move_up(obstacle_b_list[0:8:2])
        move_down(obstacle_b_list[1:8:2])

        #These functions keep the player and obstacles within a defined boundary
        obstacle_border(obstacle_b_list)
        player_border_check(player)

        #This function iterates through all level 2 obstacles and makes collisions between player and obstacles
        for i in obstacle_b_list:
            death_count = collision(i, player, death_count, death_label, level_number, 20, 60)

        #This function defines a player winning and breaks the loop moving them to the next level
        if player.xcor() > (winning_square.xcor() - 20):
            level_number += 1
            for i in obstacle_b_list:
                i.hideturtle()
            break_condition = False
    return (death_count, level_number)
