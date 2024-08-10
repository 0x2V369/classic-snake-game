from turtle import Turtle

ALIGNMENT = "center"
FONT = ("arial", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self, screen_height):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        y = (screen_height / 2) - (screen_height / (10 * 2))
        self.setposition(0, y)
        self.update_score_board()

    def update_score_board(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score_board()


    def game_over(self):
        self.setposition(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)