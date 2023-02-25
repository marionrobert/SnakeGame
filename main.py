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

# create the snake
snake = Snake()
screen.update()
screen.listen()
screen.onkey(fun=snake.go_up, key="Up")
screen.onkey(fun=snake.go_down, key="Down")
screen.onkey(fun=snake.go_right, key="Right")
screen.onkey(fun=snake.go_left, key="Left")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    # move the snake
    snake.move()


screen.exitonclick()