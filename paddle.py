from turtle import Turtle
from config import HEIGHT, PADDLE_LENGTH, PADDLE_SPEED


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        stretch = PADDLE_LENGTH / 20
        self.shapesize(stretch_len=stretch)
        self.left(90)
        self.goto(position)

    def up(self):
        if self.ycor() < (HEIGHT - PADDLE_LENGTH) / 2:
            self.forward(PADDLE_SPEED)

    def down(self):
        if self.ycor() > -(HEIGHT - PADDLE_LENGTH) / 2:
            self.back(PADDLE_SPEED)
