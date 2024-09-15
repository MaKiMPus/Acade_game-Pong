from turtle import Turtle
ALIGNMENT = "center"
FRONT = ("Courier", 20, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-20, 270)
        self.write(self.left_score, align=ALIGNMENT, font=FRONT)
        self.goto(20, 270)
        self.write(self.right_score, align=ALIGNMENT, font=FRONT)

    def add_leftscore(self):
        self.left_score += 1
        self.clear()
        self.update_scoreboard()

    def add_rightscore(self):
        self.right_score += 1
        self.clear()
        self.update_scoreboard()

