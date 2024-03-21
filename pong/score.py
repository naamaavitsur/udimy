from turtle import Turtle, Screen


class Score:

    def __init__(self, location):
        self.score_point = 0
        self.score = Turtle()
        self.score.penup()
        self.score.goto(location)
        self.score.hideturtle()
        self.score.color("white")
        self.score.write(f"{self.score_point}", False, "center", ("Arial", 100, "normal"))


    def update_score(self):
        self.score_point += 1
        self.score.clear()
        self.score.write(f"{self.score_point}", False, "center", ("Arial", 100, "normal"))
