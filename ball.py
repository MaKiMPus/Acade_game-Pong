
from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = random.randint(5, 20)
        self.y_move = random.randint(5, 20)
        self.movespeed = 0.1

    def reposition(self):
        self.goto(0,0)
        self.movespeed = 0.1

    def random_move(self):
        x_pos = self.xcor() + self.x_move
        y_pos = self.ycor() + self.y_move
        self.goto(x_pos, y_pos)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        if self.movespeed > 0.05:
            self.movespeed -= 0.005
        else:
            self.movespeed = self.movespeed

