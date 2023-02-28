from turtle import Turtle

ALIGNEMENT = "center"
FONT = ("Courier", 16, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            data_highscore = file.read()
            self.highscore = int(data_highscore)
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} - High Score: {self.highscore} ", align=ALIGNEMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        with open("data.txt", mode="w") as file:
            file.write(f"{self.highscore}")
        self.score = 0
        self.update_score()
