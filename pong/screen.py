from turtle import Turtle, Screen


class MainScreen:
    def __init__(self):
        self.middle_line = Turtle()
        self.middle_line.hideturtle()
        self.middle_line.pencolor("white")
        self.middle_line.pensize(8)
        self.middle_line.penup()
        self.middle_line.goto(0, 460)
        self.middle_line.setheading(270)
        for i in range(21):
            self.middle_line.pendown()
            self.middle_line.forward(20)
            self.middle_line.penup()
            self.middle_line.forward(25)









