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
        """
        Creates the starting snake body for the game
        If user wants a longer/shorter snake, SEGMENTS var needs to updated
        """
        for position in range(SEGMENTS):
            self.add_segment(position)

    def add_segment(self, position):
        """
        Method to create and add new segments to existing snake body
        :param position: At which part of the snake body the new segment needs to be added
        """
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.setx(SEGMENTS * 20)
        new_segment.sety(0)
        new_segment.speed("slow")
        self.snake_body.append(new_segment)

    def extend(self):
        """
        Adds a single segment at the end of the snake body
        """
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        """
        Method to move the snake body forward by MOVE_DISTANCE
        Loops through the snake body list and updates the location and direction of each segment,
        so that it is where a segment - 1 used to be
        """
        for segment in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[segment - 1].xcor()
            new_y = self.snake_body[segment - 1].ycor()
            new_heading = self.snake_body[segment - 1].heading()
            self.snake_body[segment].setheading(new_heading)
            self.snake_body[segment].setposition((new_x, new_y))
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """
        Method that is called when user presses arrow Up
        If statement makes sure that the snake does not go back on itself
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """
        Method that is called when user presses arrow Down
        If statement makes sure that the snake does not go back on itself
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """
        Method that is called when user presses arrow Left
        If statement makes sure that the snake does not go back on itself
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """
        Method that is called when user presses arrow Right
        If statement makes sure that the snake does not go back on itself
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for segment in self.snake_body:
            segment.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]
