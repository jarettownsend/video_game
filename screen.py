import turtle

#Setting up the screen
wn = turtle.Screen()
wn.title("Video Game | By Jaret Townsend")
wn.bgcolor("white")
wn.setup(width = 1000, height = 750)
wn.tracer(0)


#Setting up border class
class border(turtle.Turtle):
    def __init__(self):
       super().__init__()
       self.speed(0)
       self.color('grey')
       self.shape('square')
       self.penup()

#Setting up a function so the borders of the screen can be called later
def borders():
    border_up = border()
    border_up.shapesize(stretch_wid = .25, stretch_len = 50)
    border_up.goto(0, 350)

    border_left = border()
    border_left.shapesize(stretch_wid=30 , stretch_len=5)
    border_left.goto(-450, -75)

    border_right = border()
    border_right.shapesize(stretch_wid=30 , stretch_len=5)
    border_right.goto(450, 50)

    border_down = border()
    border_down.shapesize(stretch_wid=1.25 , stretch_len=50)
    border_down.goto(0, -362.5)

#Setting up starting/ending square class
class squares(turtle.Turtle):
    def __init__(self):
       super().__init__()
       self.speed(0)
       self.color('green')
       self.shape('square')
       self.penup()


#These squares will be sent to their positions on the screen
starting_square = squares()
starting_square.goto(-450, 286.25)
starting_square.shapesize(stretch_wid=6.125, stretch_len=5)

winning_square = squares()
winning_square.goto(450,-300)
winning_square.shapesize(stretch_wid=5, stretch_len=5)
