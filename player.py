import turtle
from screen import wn, starting_square

#Player object. It spawns wherever the starting square is located
player = turtle.Turtle()
player.speed(0)
player.shape('circle')
player.color('blue')
player.penup()
player.goto(starting_square.xcor(), starting_square.ycor())

#Player Movement Functions
def player_up():
    y = player.ycor()
    y += 15
    player.sety(y)

def player_down():
    y = player.ycor()
    y -= 15
    player.sety(y)

def player_right():
    x = player.xcor()
    x += 15
    player.setx(x)

def player_left():
    x = player.xcor()
    x -= 15
    player.setx(x)

#Keyoard inputs
wn.listen()
wn.onkeypress(player_up, "Up")
wn.onkeypress(player_down, "Down")
wn.onkeypress(player_right, "Right")
wn.onkeypress(player_left, "Left")
