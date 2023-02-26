from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# set tup the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")


# Turn turtle animation on/off and set delay for update drawings.
screen.tracer(0)

# create the snake, food and scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.update()

# controle snake with a keypress
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
    # detect collision with food
    if snake.head.distance(food) < 15:
        print("you've got food")
        food.refresh()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 288 \
            or snake.head.xcor() < -288 \
            or snake.head.ycor() > 288 \
            or snake.head.ycor() < -288:
        game_on = False
        scoreboard.game_over()



screen.exitonclick()