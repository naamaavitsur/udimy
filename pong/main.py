from turtle import Screen
import time
from screen import MainScreen
from score import Score
from disc import Disc
from ball import Ball
import config

if __name__ == '__main__':
    game_is_on = True
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(config.SCREEN_X_SIZE, config.SCREEN_Y_SIZE)
    screen.tracer(0)
    main_screen = MainScreen()
    left_score = Score((-100, 350))
    right_score = Score((100, 350))
    disc_right = Disc((700, 0), screen)
    disc_left = Disc((-700, 0), screen)
    ball = Ball()
    # left_score.update_score()
    screen.listen()
    disc_left.move_disc("Up", "Down")
    disc_right.move_disc("a", "z")

    while game_is_on:
        screen.update()
        screen.tracer(1)
        ball.find_new_direction_for_ball(0, 360)
        if ball.ball.ycor() > 485 and ball.ball.ycor() < -480:
            ball.find_new_direction_for_ball(180,360)



    screen.exitonclick()


