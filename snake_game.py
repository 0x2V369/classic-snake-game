from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
game_is_on = True

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Classic Snake Game")
screen.tracer(0)

snake = Snake()
food = Food(SCREEN_WIDTH, SCREEN_HEIGHT)
score_board = ScoreBoard(SCREEN_HEIGHT)

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:

    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score_board.game_over()

    # Detect collision with tale
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()

screen.exitonclick()
