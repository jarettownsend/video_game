import turtle

#Defining obstacle_b class
class obstacle_b(turtle.Turtle):
     def __init__(self):
        super().__init__()
        self.speed(0)
        self.color('red')
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=1 , stretch_len=5)
        self.dx = 2.5
        self.dy = 2.5

#Setting up obstacles based on obstacle_b class
obstacle1b = obstacle_b()
obstacle1b.goto(-350, 0)

obstacle2b = obstacle_b()
obstacle2b.goto(-250, 0)

obstacle3b = obstacle_b()
obstacle3b.goto(-150, 0)

obstacle4b = obstacle_b()
obstacle4b.goto(-50, 0)

obstacle5b = obstacle_b()
obstacle5b.goto(50, 0)

obstacle6b = obstacle_b()
obstacle6b.goto(150, 0)

obstacle7b = obstacle_b()
obstacle7b.goto(250, 0)

obstacle8b = obstacle_b()
obstacle8b.goto(350, 0)


#Setting up Obstacle List
obstacle_b_list = [obstacle1b, obstacle2b, obstacle3b, obstacle4b, obstacle5b, obstacle6b, obstacle7b, obstacle8b]
