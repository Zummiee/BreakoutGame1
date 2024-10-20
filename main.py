from turtle import Screen, Turtle
import time
import random
from ball import Ball
from paddle import Paddle
from wall_manager import Brick
from scoreboard import Scoreboard

screen = Screen()
screen.title("BreakOut Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
ball = Ball()
paddle = Paddle()
scoreboard = Scoreboard()
screen.listen()
screen.colormode(1)
screen.onkey(key="Right", fun=paddle.move_right)
screen.onkey(key="Left", fun=paddle.move_left)


def get_random_color():
    r = random.randint(0, 255) / 255
    g = random.randint(0, 255) / 255
    b = random.randint(0, 255) / 255
    return (r, g, b)


bricks = []
latest_y = 180
n = 0

for _ in range(5):
    latest_x = -360
    latest_y -= 30
    for _ in range(10):
        brick = Brick(color=get_random_color(), x=latest_x, y=latest_y)
        latest_x += 80
        bricks.append(brick)

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    for brick in bricks:
        brick_x, brick_y = brick.pos()
        if n != 0 and n % 8 == 0:
            ball.speed += 1
        if brick_y - ball.ycor() < 20 and -40 < ball.xcor() - brick_x < 40:
            n += 1
            brick.hideturtle()
            bricks.remove(brick)
            ball.change_y_direction()
            scoreboard.score = 50 - len(bricks)
            scoreboard.score_update()
            if not bricks:
                scoreboard.announce_win()
                ball.hideturtle()
                game_is_on = False
            break
    if ball.ycor() - paddle.ycor() < 20 and -100 < ball.xcor() - paddle.xcor() < 100:
        ball.change_y_direction()
    if ball.xcor() <= -390:
        ball.change_x_direction()
    if ball.xcor() >= 390:
        ball.change_x_direction()
    if ball.ycor() >= 290:
        ball.change_y_direction()
    if ball.ycor() < -280 and -380 < ball.xcor() < 380:
        scoreboard.game_over()
        ball.hideturtle()
        game_is_on = False
    time.sleep(0.004)

screen.exitonclick()
