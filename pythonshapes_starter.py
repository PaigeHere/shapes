from turtle import *
import math
import time

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,500)
x_pos = -250
y_pos = -150
t.setposition(x_pos, y_pos)

### Write your code below:

circle(100)
reset()


for i in range (4):
    forward(50)
    right(90)

reset()

for i in range (3):
    forward (100)
    right(120)

def draw():
    reset()
    sides= int (input("enter a number: "))
    colors= input("enter a color: ")
    steps= int (input("enter a number value for distance: "))
    fillcolor(colors)
    begin_fill()
    for i in range (sides):
        pencolor(colors)
        forward(steps)
        right (180-((sides-2)*180/sides))
    end_fill()
    time.sleep(2)

for i in range(3):
    draw()


# Close window on click.
exitonclick()
