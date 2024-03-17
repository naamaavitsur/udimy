from turtle import Turtle


class Snake:

    def __init__(self, screen):
        self.screen = screen
        self.list_of_where_start_snake = [(-40, 0), (-20, 0), (0, 0)]
        self.list_of_snakes = []

    def snake(self):
        self.place = 0
        for goto in self.list_of_where_start_snake:
            snake_segment = Turtle("square")
            snake_segment.color("red")
            snake_segment.penup()
            snake_segment.speed("fast")
            snake_segment.goto(self.list_of_where_start_snake[self.place])
            self.place += 1
            self.list_of_snakes.append(snake_segment)

    def add_segment(self):
        snake_segment = Turtle("square")
        snake_segment.color("red")
        snake_segment.penup()
        snake_segment.speed("fast")
        self.list_of_snakes.append(snake_segment)

    # def extend_snake(self):

    def move(self):
        def turn_left():
            if self.list_of_snakes[2].heading() != 0:
                self.list_of_snakes[2].setheading(180)

        def turn_right():
            if self.list_of_snakes[2].heading() != 180:
                self.list_of_snakes[2].setheading(0)

        def turn_up():
            if self.list_of_snakes[2].heading() != 270:
                self.list_of_snakes[2].setheading(90)

        def turn_down():
            if self.list_of_snakes[2].heading() != 90:
                self.list_of_snakes[2].setheading(270)

        self.screen.onkey(turn_left, "Left")
        self.screen.onkey(turn_right, "Right")
        self.screen.onkey(turn_up, "Up")
        self.screen.onkey(turn_down, "Down")

        for i in range(0, len(self.list_of_snakes) - 1, 1):
            segment_x = self.list_of_snakes[i - 1].xcor()
            segment_y = self.list_of_snakes[i - 1].ycor()
            self.list_of_snakes[i].goto(segment_x, segment_y)
        self.list_of_snakes[2].forward(20)