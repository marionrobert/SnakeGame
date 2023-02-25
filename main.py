from turtle import Screen, Turtle
import time
from snake import Snake

# set tup the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# Turn turtle animation on/off and set delay for update drawings.
screen.tracer(0)
game_on = True

# create the snake
snake = Snake()

screen.update()

while game_on:
    screen.update()
    time.sleep(0.1)
    # move the snake
    snake.move()


screen.exitonclick()