from turtle import Turtle

SEGMENTS = 3
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in range(SEGMENTS):
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.setx(SEGMENTS * 20)
        new_segment.sety(0)
        new_segment.speed("slow")
        self.snake_body.append(new_segment)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        for segment in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[segment - 1].xcor()
            new_y = self.snake_body[segment - 1].ycor()
            new_heading = self.snake_body[segment - 1].heading()
            self.snake_body[segment].setheading(new_heading)
            self.snake_body[segment].setposition((new_x, new_y))
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
