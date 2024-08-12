from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard

# Setting up screen dimensions for the game
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
game_is_on = True

# Initializing Turtle Screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Classic Snake Game")
screen.tracer(0)

# Creating snake, food and socre_board objects
snake = Snake()
food = Food(SCREEN_WIDTH, SCREEN_HEIGHT)
score_board = ScoreBoard(SCREEN_HEIGHT)

# Setting up screen for the user inputs to navigate the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main loop for the game
while game_is_on:

    # Screen update after every iteration in the while loop with a time delay for smoother graphics
    screen.update()
    time.sleep(0.1)

    # Move the snake forward
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.reset()
        snake.reset()

    # Detect collision with tale
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()


# Screen closes if user clicks anywhere on it
screen.exitonclick()
