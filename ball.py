from turtle import Turtle
import random

MIDDLE_DEAD_ZONE = 60


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.wait = 0
        self.reset_position()

    def reset_position(self):
        self.goto(0, 0)
        direction = random.random() * 360
        while (90 - MIDDLE_DEAD_ZONE / 2 < direction < 90 + MIDDLE_DEAD_ZONE / 2) \
                or (270 - MIDDLE_DEAD_ZONE / 2 < direction < 270 + MIDDLE_DEAD_ZONE / 2):
            direction = random.random() * 360
        self.setheading(direction)
        self.wait = 15

    def bounce_horizontally(self):
        self.setheading(360 - self.heading())

    def bounce_vertically(self):
        self.setheading(180 - self.heading())

    def move(self):
        if self.wait > 0:
            self.wait -= 1
        else:
            self.forward(10)
