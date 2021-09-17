from turtle import Screen
from config import WIDTH, HEIGHT
from paddle import Paddle
from time import sleep

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Pong.")
screen.tracer(0)

position_left = (-WIDTH / 2 + 50, 0)
paddle_left = Paddle(position_left)
position_right = (WIDTH / 2 - 50, 0)
paddle_right = Paddle(position_right)


screen.onkeypress(key="w", fun=paddle_left.up)
screen.onkeypress(key='s', fun=paddle_left.down)
screen.onkeypress(key='Up', fun=paddle_right.up)
screen.onkeypress(key='Down', fun=paddle_right.down)
screen.listen()

game_is_on = True
while game_is_on:
    sleep(0.01)
    screen.update()

screen.exitonclick()