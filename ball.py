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
        self.wait = 0

    def reset_position(self):
        self.goto(0, 0)
        direction = random.random() * 360
        while (80 < direction < 100) or (260 < direction < 280):
            direction = random.random() * 360
        self.setheading(direction)

    def bounce_horizontally(self):
        self.setheading(360 - self.heading())

    def bounce_vertically(self):
        self.setheading(180 - self.heading())

    def move(self):
        if self.wait > 0:
            self.wait -= 1
        else:
            self.forward(10)
