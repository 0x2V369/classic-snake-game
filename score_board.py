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
        y = (screen_height / 2) - 50
        self.setposition(0, y)
        self.high_score = 0
        self.get_high_score()
        self.update_score_board()

    def update_score_board(self):
        """
        Method to update the score board with current result
        """
        self.clear()
        self.write(f"Score: {self.score} Highest Score:{self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """
        Method called when snake hits the food object
        clear() removes the old .write() text and replaces with the new one from method update_score_board()
        """
        self.score += 1
        self.update_score_board()

    def reset(self):
        """
        Method for resetting the score to zero and updating the highest score if it was higher
        """
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.update_score_board()

    def get_high_score(self):
        """Get the highest historical score from the data.txt file """
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())

    def write_high_score(self):
        """Log new highest score to the data file"""
        with open("data.txt", mode="w") as data:
            data.write(f"{self.high_score}")
