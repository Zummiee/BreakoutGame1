from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("green")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.goto(x=0, y=-230)
        self.speed = 0

    def move_right(self):
        new_x = self.xcor() + 30
        self.goto(x=new_x, y=self.ycor())

    def move_left(self):
        new_x = self.xcor() - 30
        self.goto(x=new_x, y=self.ycor())
