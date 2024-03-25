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
        self.high_score = 0

    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
        self.score = 0
        self.increase_score()



    def pluse_one(self):
        self.score += 1

    def increase_score(self):
        self.title.goto(0, 280)
        self.title.color("white")
        self.title.clear()
        self.title.write(f"Score: {self.score}, High score:{self.high_score}", False, ALIGNMENT,
                         FONT)


    def game_over(self):
        self.title.goto(0, 0)
        self.title.write("GAME OVER", False, ALIGNMENT,
                         FONT)


if __name__ == '__main__':
    score = Score()
    score.increase_score(1)
    screen = Screen()
    screen.exitonclick()