from turtle import Turtle


class Level(Turtle):

    def __init__(self, level_number):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-250, 270)
        self.write(f"Level: {level_number}", False, "center", ("Arial", 12, "normal"))