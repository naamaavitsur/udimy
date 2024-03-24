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
    disc_left.move_disc("a", "z")
    disc_right.move_disc("Up", "Down")

    while game_is_on:
        time.sleep(0.02)
        screen.update()
        ball.move()
        if ball.ball.ycor() > 480 or ball.ball.ycor() < -480:
            ball.bounce_hit_y()
        elif ball.ball.distance(disc_right.disc) < 50 and ball.ball.xcor() > 670 or ball.ball.distance(disc_left.disc) < 50 and ball.ball.xcor() > -740:
            ball.bounce_hit_x()
        elif ball.ball.xcor() > 750:
            right_score.update_score()
            screen.tracer(0)
            ball.bounce_hit_x()
            ball.ball.goto(0, 0)
        elif ball.ball.xcor() < -750:
            left_score.update_score()
            ball.bounce_hit_x()
            screen.tracer(0)
            ball.ball.goto(0, 0)
        elif left_score.score_point == 10 or right_score.score_point == 10:
            game_is_on = False











    screen.exitonclick()


