from turtle import Turtle

class PlayerTurtle(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(0, -270)

    def move(self):
        self.forward(20)
