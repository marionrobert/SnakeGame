from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.create_scoreboard()

    def create_scoreboard(self):
        self.hideturtle()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 16, "normal"))

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("Arial", 16, "normal"))
