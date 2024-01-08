from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

winning_score = 6

# set up the playground
screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

line = Turtle()
line.hideturtle()
line.pencolor("white")
line.pensize(3)
line.penup()
line.goto(0, 295)
line.setheading(270)
for n in range(15):
    line.pendown()
    line.forward(20)
    line.penup()
    line.forward(20)

# create players --> player_right and player_left
player_right = Paddle((410, 0))
player_left = Paddle((-410, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.update()

screen.listen()
screen.onkeypress(fun=player_right.move_up, key="Up")
screen.onkeypress(fun=player_right.move_down, key="Down")
screen.onkeypress(fun=player_left .move_up, key="z")
screen.onkeypress(fun=player_left .move_down, key="q")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with the wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # detect collision with paddles
    if ball.distance(player_right) < 60 and ball.xcor() > 380\
            or ball.distance(player_left ) < 60 and ball.xcor() < -380:
        ball.bounce_x()

    # detect if paddle misses the ball
    if ball.xcor() > 435:
        scoreboard.increase_left_score()
        ball.go_center()

    if ball.xcor() < -435:
        scoreboard.increase_right_score()
        ball.go_center()

    # detect game over
    if scoreboard.player_left_score == winning_score or scoreboard.player_right_score == winning_score:
        scoreboard.game_over(winning_score)
        game_on = False

screen.exitonclick()
