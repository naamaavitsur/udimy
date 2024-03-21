from turtle import Turtle
import random
import config

class Ball:
    def __init__(self):
        self.ball = Turtle("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.speed(2)

    def find_new_direction_for_ball(self, from_angle, to_angle):
        self.ball.forward(5)
        ball_direction_angle = random.randint(from_angle,to_angle)
        self.ball.setheading(ball_direction_angle)
        while self.ball.ycor() < 480 and self.ball.ycor() > -480:
            self.ball.forward(5)

