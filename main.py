from turtle import Screen
from config import WIDTH, HEIGHT, PADDLE_LENGTH, GAME_SPEED, WIN_POINTS
from paddle import Paddle
from time import sleep
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Pong.")
screen.tracer(0)

position_left = (-WIDTH / 2 + 50, 0)
paddle_left = Paddle(position_left)
position_right = (WIDTH / 2 - 50, 0)
paddle_right = Paddle(position_right)

ball = Ball()

score_left = Scoreboard((-60, HEIGHT / 2 - 60))
score_right = Scoreboard((60, HEIGHT / 2 - 60))

screen.onkeypress(key="w", fun=paddle_left.up)
screen.onkeypress(key='s', fun=paddle_left.down)
screen.onkeypress(key='Up', fun=paddle_right.up)
screen.onkeypress(key='Down', fun=paddle_right.down)
screen.listen()

game_is_on = True
while game_is_on:
    sleep(GAME_SPEED)
    screen.update()
    ball.move()
    if abs(ball.ycor()) >= HEIGHT / 2 - 20:
        ball.bounce_horizontally()

    # Detect bounce with left paddle
    if 10 < ball.xcor() - paddle_left.xcor() < 20 and abs(ball.ycor() - paddle_left.ycor()) < PADDLE_LENGTH / 2 + 2:
        ball.bounce_vertically()

    if 10 < paddle_right.xcor() - ball.xcor() < 20 and abs(ball.ycor() - paddle_right.ycor()) < PADDLE_LENGTH / 2 + 2:
        ball.bounce_vertically()

    if abs(ball.xcor()) >= WIDTH / 2:
        if ball.xcor() >= WIDTH / 2:
            score_left.add_score()
            if score_left.score == WIN_POINTS:
                game_is_on = False
        else:
            score_right.add_score()
            if score_right.score == WIN_POINTS:
                game_is_on = False
        ball.reset_position()

ball.reset_position()
screen.update()
screen.exitonclick()