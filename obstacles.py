import turtle

#This class defines square obstacles and their speeds
class obstacle(turtle.Turtle):
     def __init__(self):
        super().__init__()
        self.speed(0)
        self.color('red')
        self.shape('square')
        self.penup()
        self.dx = 2.5
        self.dy = 2.5

#These sub classes create obstacles and move them to a position on the screen
obstacle1 = obstacle()
obstacle1.goto(0, 200)

obstacle2 = obstacle()
obstacle2.goto(0, 160)

obstacle3 = obstacle()
obstacle3.goto(0, 120)

obstacle4 = obstacle()
obstacle4.goto(0, 80)

obstacle5 = obstacle()
obstacle5.goto(0, 40)

obstacle6 = obstacle()
obstacle6.goto(0, 0)

obstacle7 = obstacle()
obstacle7.goto(0, -40)

obstacle8 = obstacle()
obstacle8.goto(0, -80)

obstacle9 = obstacle()
obstacle9.goto(0, -120)

obstacle10 = obstacle()
obstacle10.goto(0, -160)

obstacle11 = obstacle()
obstacle11.goto(0, -200)

obstacle12 = obstacle()
obstacle12.goto(0, -240)

#This obstacles will move vertically
obstacle13 = obstacle()
obstacle13.goto(-350, -1.25)

obstacle14 = obstacle()
obstacle14.goto(-300, -1.25)

obstacle15 = obstacle()
obstacle15.goto(-250, -1.25)

obstacle16 = obstacle()
obstacle16.goto(-200, -1.25)

obstacle17 = obstacle()
obstacle17.goto(-150, -1.25)

obstacle18 = obstacle()
obstacle18.goto(-100, -1.25)

obstacle19 = obstacle()
obstacle19.goto(-50, -1.25)

obstacle20 = obstacle()
obstacle20.goto(50, -1.25)

obstacle21 = obstacle()
obstacle21.goto(100, -1.25)

obstacle22 = obstacle()
obstacle22.goto(150, -1.25)

obstacle23 = obstacle()
obstacle23.goto(200, -1.25)

obstacle24 = obstacle()
obstacle24.goto(250, -1.25)

obstacle25 = obstacle()
obstacle25.goto(300, -1.25)

obstacle26 = obstacle()
obstacle26.goto(350, -1.25)

#Setting up Obstacle List
#Setting this list up will make it possible to iterate through all of the obstacles so they don't have to be call them individually
obstacle_list = [obstacle1, obstacle2, obstacle3, obstacle4, obstacle5, obstacle6, obstacle7, obstacle8, obstacle9, obstacle10, obstacle11, obstacle12, obstacle13, obstacle14, obstacle15, obstacle16, obstacle17, obstacle18, obstacle19, obstacle20, obstacle21, obstacle22, obstacle23, obstacle24, obstacle25, obstacle26]
