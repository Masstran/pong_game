from turtle import Turtle
import random
from config import UPPER_BOUND, LOWER_BOUND, RIGHT_BOUND, LEFT_BOUND


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.reset_position()

    def reset_position(self):
        self.goto(0, 0)
        direction = random.random() * 360
        self.setheading(direction)

    def correct_heading(self):
        if abs(self.ycor()) >= UPPER_BOUND - 10:
            self.setheading(360 - self.heading())

        if abs(self.xcor()) >= RIGHT_BOUND:
            self.reset_position()

    def move(self):
        self.correct_heading()
        self.forward(10)
