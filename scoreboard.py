from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(x=320, y=250)
        self.score = 0
        self.pencolor("white")
        self.write(f"Score: {self.score}", font=("Arial", 20, "bold"), align="center")
        self.hideturtle()

    def score_update(self):
        self.clear()
        self.write(f"Score: {self.score}", font=("Arial", 20, "bold"), align="center")

    def announce_win(self):
        self.goto(0,0)
        self.write("Congrats, you are free!", font=("Arial", 24, "bold"), align="center")

    def game_over(self):
        self.goto(0,250)
        self.write("Game Over", font=("Arial", 24, "bold"), align="center")