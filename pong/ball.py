from turtle import Turtle
import random
import config

class Ball:

    def __init__(self):
        self.ball = Turtle("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.speed(2)
        self.ball_x_move = 10
        self.ball_y_move = 10


    # def find_new_direction_for_ball(self, from_angle, to_angle):
    #     ball_direction_angle = random.randint(from_angle, to_angle)
    #     self.ball.setheading(ball_direction_angle)

    def move(self):
        new_y = self.ball.ycor() + self.ball_y_move
        new_x = self.ball.xcor() + self.ball_x_move
        self.ball.goto(new_x, new_y)

    def bounce_hit_y(self):
        self.ball_y_move *= -1

    def bounce_hit_x(self):
        self.ball_x_move *= -1

















