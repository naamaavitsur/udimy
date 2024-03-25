from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import Score

if __name__ == '__main__':
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=600, height=600)
    screen.title("NAAMA'S SNAKE GAME")
    screen.listen()
    game_is_on = True
    snake = Snake(screen)
    snake.snake()
    food = Food()
    score = Score()
    score.increase_score()

    while game_is_on:
        time.sleep(0.019)
        snake.move()
        if snake.list_of_snakes[-1].distance(food) < 15:
            food.refresh_food()
            score.pluse_one()
            score.increase_score()
            snake.add_segment()
        elif snake.list_of_snakes[-1].xcor() > 280 or snake.list_of_snakes[-1].xcor() < -280 or snake.list_of_snakes[-1].ycor() > 280 or snake.list_of_snakes[-1].ycor() < -280:
            score.reset()
            snake.reset()
        for segment in snake.list_of_snakes[:-1]:
            if snake.list_of_snakes[-1].distance(segment) < 10:
                score.reset()
                snake.reset()

    screen.exitonclick()
