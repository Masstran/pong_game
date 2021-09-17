from turtle import Turtle
from config import HEIGHT
ALIGNMENT = 'center'
FONT = ('Courier', 40, 'bold')

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.score = 0
        self.goto(position)
        self.hideturtle()
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(self.score, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.refresh()
