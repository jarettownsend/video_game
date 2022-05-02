import turtle


#These variables were created on the main script because they will be passed through each level
death_count = 0
level_number = 1


death_label = turtle.Turtle()
death_label.speed(0)
death_label.color('blue')
death_label.penup()
death_label.hideturtle()
death_label.goto(0, 350)
death_label.write(f'Level {level_number}/3 | Deaths: {death_count}', align='center', font=("Courier", 24, "normal"))


from level_1 import *
death_count, level_number = level1(int(death_count), death_label, level_number)


from level_2 import *
death_count, level_number = level2(int(death_count), death_label, level_number)


from level_3 import *
death_count, level_number = level3(int(death_count), death_label, level_number)
