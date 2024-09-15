from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

x_wall = [range(-350,350,1)]
y_upperwall = [300]
y_lowerwall = [-300]


game_on = True
while game_on:
    time.sleep(ball.movespeed)
    screen.update()
    ball.random_move()

    ##Detect collision with the wall and bounce
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    ##Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    if ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    ##Detect when the paddle misses
    if ball.xcor() > 350:
        score.add_leftscore()
        ball.reposition()
 
    if ball.xcor() < -350:
        score.add_rightscore()
        ball.reposition()

screen.exitonclick()