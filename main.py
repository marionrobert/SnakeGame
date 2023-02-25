from turtle import Screen, Turtle
import time

# set tup the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# Turn turtle animation on/off and set delay for update drawings.
screen.tracer(0)
game_on = True

# create the snake
positions = [(0, 0), (-20, 0), (-40, 0)]
all_segments = []

for position in positions:
    new_segment = Turtle(shape="square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(position)
    all_segments.append(new_segment)

screen.update()

while game_on:
    screen.update()
    time.sleep(0.1)
    # move the snake
    for seg_num in range((len(all_segments) - 1), 0, -1):
        new_x = all_segments[seg_num - 1].xcor()
        new_y = all_segments[seg_num - 1].ycor()
        all_segments[seg_num].goto(new_x, new_y)
    all_segments[0].forward(20)


screen.exitonclick()