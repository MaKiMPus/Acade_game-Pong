from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import random


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
# screen.tracer(0)

paddle = Turtle(shape="square")
paddle.color("white")
paddle.penup()
paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle = paddle.goto((350, 0))

paddle = Turtle(shape="square")
paddle.color("white")
paddle.penup()
paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle = paddle.goto((-350, 0))

def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(go_up, "w")
screen.onkey(go_down, "s")
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")


#
# is_game_on = True
# while is_game_on:
#     screen.update()

screen.exitonclick()