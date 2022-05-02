import turtle

#Defining obstacle_c class
class obstacle_c(turtle.Turtle):
     def __init__(self):
        super().__init__()
        self.speed(0)
        self.color('red')
        self.shape('square')
        self.penup()
        self.dx = 2.5
        self.dy = 2.5

#Creating obstacles that spawn along left wall
obstacle1c = obstacle_c()
obstacle1c.goto(-390, -340)

obstacle2c = obstacle_c()
obstacle2c.goto(-390, -300)

obstacle3c = obstacle_c()
obstacle3c.goto(-390, -260)

obstacle4c = obstacle_c()
obstacle4c.goto(-390, -220)

obstacle5c = obstacle_c()
obstacle5c.goto(-390, -180)

obstacle6c = obstacle_c()
obstacle6c.goto(-390, -140)

obstacle7c = obstacle_c()
obstacle7c.goto(-390, -100)

obstacle8c = obstacle_c()
obstacle8c.goto(-390, -60)

obstacle9c = obstacle_c()
obstacle9c.goto(-390, -20)

obstacle10c = obstacle_c()
obstacle10c.goto(-390, 20)

#Creating obstacles that spawn along right wall
obstacle11c = obstacle_c()
obstacle11c.goto(390, 337.5)

obstacle12c = obstacle_c()
obstacle12c.goto(390, 297.5)

obstacle13c = obstacle_c()
obstacle13c.goto(390, 257.5)

obstacle14c = obstacle_c()
obstacle14c.goto(390, 217.5)

obstacle15c = obstacle_c()
obstacle15c.goto(390, 177.5)

obstacle16c = obstacle_c()
obstacle16c.goto(390, 137.5)

obstacle17c = obstacle_c()
obstacle17c.goto(390, 97.5)

obstacle18c = obstacle_c()
obstacle18c.goto(390, 57.5)

obstacle19c = obstacle_c()
obstacle19c.goto(390, 17.5)

obstacle20c = obstacle_c()
obstacle20c.goto(390, 20)

#Creating obstacles that spawn along bottom wall
obstacle21c = obstacle_c()
obstacle21c.goto(390, -340)

obstacle22c = obstacle_c()
obstacle22c.goto(350, -340)

obstacle23c = obstacle_c()
obstacle23c.goto(310, -340)

obstacle24c = obstacle_c()
obstacle24c.goto(270, -340)

obstacle25c = obstacle_c()
obstacle25c.goto(230, -340)

obstacle26c = obstacle_c()
obstacle26c.goto(190, -340)

obstacle27c = obstacle_c()
obstacle27c.goto(150, -340)

obstacle28c = obstacle_c()
obstacle28c.goto(110, -340)

obstacle29c = obstacle_c()
obstacle29c.goto(70, -340)

obstacle30c = obstacle_c()
obstacle30c.goto(30, -340)

#Creating obstacles that spawn along top wall
obstacle31c = obstacle_c()
obstacle31c.goto(-390, 337.5)

obstacle32c = obstacle_c()
obstacle32c.goto(-350, 337.5)

obstacle33c = obstacle_c()
obstacle33c.goto(-310, 337.5)

obstacle34c = obstacle_c()
obstacle34c.goto(-270, 337.5)

obstacle35c = obstacle_c()
obstacle35c.goto(-230, 337.5)

obstacle36c = obstacle_c()
obstacle36c.goto(-190, 337.5)

obstacle37c = obstacle_c()
obstacle37c.goto(-150, 337.5)

obstacle38c = obstacle_c()
obstacle38c.goto(-110, 337.5)

obstacle39c = obstacle_c()
obstacle39c.goto(-70, 337.5)

obstacle40c = obstacle_c()
obstacle40c.goto(-30, 337.5)

#Setting up obstacle list
obstacle_c_list = [obstacle1c, obstacle2c, obstacle3c, obstacle4c, obstacle5c, obstacle6c, obstacle7c, obstacle8c, obstacle9c, obstacle10c, obstacle11c, obstacle12c, obstacle13c, obstacle14c, obstacle15c, obstacle16c, obstacle17c, obstacle18c, obstacle19c, obstacle20c, obstacle21c, obstacle22c, obstacle23c, obstacle24c, obstacle25c, obstacle26c, obstacle27c, obstacle28c, obstacle29c, obstacle30c, obstacle31c, obstacle32c, obstacle33c, obstacle34c, obstacle35c, obstacle36c, obstacle37c, obstacle38c, obstacle39c, obstacle40c]
