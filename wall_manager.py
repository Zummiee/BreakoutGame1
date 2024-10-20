from turtle import Turtle


class Brick(Turtle):
    def __init__(self, color, x, y):
        super().__init__()
        self.penup()
        self.color(color)
        self.shape("square")
        self.shapesize(stretch_wid=1.5, stretch_len=4)
        self.goto(x, y)
