from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.screen_width = screen_width
        self.screen_height = screen_height
        random_x = random.randint(-((self.screen_width * 0.5) - 20), ((self.screen_width * 0.5) - 20))
        random_y = random.randint(-((self.screen_height * 0.5) - 20), ((self.screen_height * 0.5) - 20))
        self.goto(random_x, random_y)

    def refresh(self):
        random_x = random.randint(-((self.screen_width * 0.5) - 20), ((self.screen_width * 0.5) - 20))
        random_y = random.randint(-((self.screen_height * 0.5) - 20), ((self.screen_height * 0.5) - 20))
        self.goto(random_x, random_y)
