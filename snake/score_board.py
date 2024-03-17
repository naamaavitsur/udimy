from turtle import Turtle, Screen

ALIGNMENT = "center"
FONT = ("Ariel", 12, "normal")


class Score:

    def __init__(self):
        self.title = Turtle("square")
        self.title.penup()
        self.title.speed("fastest")
        self.title.shapesize(0.5, 2, 2)
        self.title.hideturtle()
        self.score = 0

    def pluse_one(self):
        self.score += 1

    def increase_score(self):
        self.title.goto(0, 280)
        self.title.color("white")
        self.title.clear()
        self.title.write(f"score: {self.score}", False, ALIGNMENT,
                         FONT)
        self.pluse_one()

    def game_over(self):
        self.title.goto(0, 0)
        self.title.write("GAME OVER", False, ALIGNMENT,
                         FONT)


if __name__ == '__main__':
    score = Score()
    score.increase_score(1)
    screen = Screen()
    screen.exitonclick()