import time
from turtle import Turtle,Screen
import random
screen = Screen()

class Cars():

    def __init__(self):
        self.list_of_cars = []

    def create_cars(self):
        color_list = ["red", "green", "yellow", "blue", "brown", "purple"]
        screen.tracer(0)
        new_car = Turtle()
        new_car.penup()
        new_car.goto(300, random.randint(-250, 250))
        new_car.shape("square")
        new_car.shapesize(1, 2)
        new_car.color(random.choice(color_list))
        self.list_of_cars.append(new_car)
        screen.update()


    def game_over(self):
        game_over = Turtle()
        game_over.write("GAME OVER! looser", False, "center", ("Arial", 20, "normal"))







if __name__ == '__main__':
    car = Cars()
    screen.exitonclick()








