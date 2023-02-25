from turtle import Screen, Turtle

# set tup the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")


# create the snake
positions = [(0, 0), (-20, 0), (-40, 0)]
snake = []

for position in positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.goto(position)
    snake.append(new_segment)



screen.exitonclick()