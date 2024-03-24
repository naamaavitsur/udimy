from turtle import Turtle, Screen
import random
from level import Level
from player_turtle import PlayerTurtle
from cars import Cars
import time

level_number = 1
game_is_on = True
timer_create_cars = 6
time_sleep = 0.1
screen = Screen()
screen.tracer(0)
screen.setup(600, 600)
screen.listen()
level_update = Level(level_number)
player_turtle = PlayerTurtle()
screen.onkey(player_turtle.move, "Up")
car_meneger = Cars()

while game_is_on:
    time.sleep(time_sleep)
    screen.update()
    if timer_create_cars % 6 == 0:
        car_meneger.create_cars()
    for i in car_meneger.list_of_cars:
        new_x = i.xcor() - 20
        i.goto(new_x, i.ycor())
        if player_turtle.distance(i) < 20:
            car_meneger.game_over()
            game_is_on = False
    if player_turtle.ycor() > 270:
        screen.update()
        player_turtle.goto(0, -270)
        level_number += 1
        level_update.clear()
        level_update = Level(level_number)
        time_sleep -= 0.02
    timer_create_cars += 1














screen.exitonclick()
