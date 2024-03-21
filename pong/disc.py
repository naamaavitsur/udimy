from turtle import Turtle, Screen
import config


class Disc:
    def __init__(self, location, screen):
        self.screen = screen
        self.disc = Turtle()
        self.disc.penup()
        self.disc.shape("square")
        self.disc.color("red")
        self.disc.shapesize(config.DISC_SIZE_Y, config.DISC_SIZE_X)
        self.disc.goto(location)

    def move_disc(self, key_up, key_down):

        def turn_up():
            if self.disc.ycor() < config.SCREEN_Y_SIZE / 2 - config.DISC_SIZE_Y * 10:
                new_y = self.disc.ycor() + config.MOVE_DISC_PACE
                self.disc.goto(self.disc.xcor(), new_y)

        def turn_down():
            if self.disc.ycor() > -(config.SCREEN_Y_SIZE/2 - config.DISC_SIZE_Y*10):
                new_y = self.disc.ycor() - config.MOVE_DISC_PACE
                self.disc.goto(self.disc.xcor(), new_y)


        self.screen.onkey(turn_up, key_up)
        self.screen.onkey(turn_down, key_down)



# if __name__ == '__main__':
#     screen = Screen()
#     nice = Disc((100,100),screen)
#     nice.move_disc()
#
#     screen.exitonclick()




