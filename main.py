from turtle import Screen
from config import WIDTH, HEIGHT
from paddle import Paddle
from time import sleep

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Pong.")
screen.tracer(0)

position1 = (-WIDTH / 2 + 30, 0)
paddle1 = Paddle(position1)
screen.update()

game_is_on = True
while game_is_on:
    sleep(0.1)
    screen.update()

screen.exitonclick()