from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto(x=0, y=-210)
        self.speed = 1
        self.move_x = 3
        self.move_y = 3

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def change_y_direction(self):
        self.move_y *= -1

    def change_x_direction(self):
        self.move_x *= -1
