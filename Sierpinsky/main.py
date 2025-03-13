import turtle
from my_math import *
from squares import get_squares
from colors import get_color
from typing import Tuple
type point = Tuple[float, float]
type square = Tuple[point, point, point, point]


scale: int = 9
squares = get_squares(scale)

# Set up drawing canvas
win_size: int = round(power_of_two(scale + 1))
turtle.setup(win_size, win_size)

window = turtle.Screen()
window.bgcolor("black")
window.title("Sierpinski Square")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()


def draw_square(index: int, sq: square) -> None:

    color: str = get_color(index)
    t.fillcolor(color)
    points: list = list(sq)
    first = points.pop()  # move from the start ...
    points.append(first)  # to the end:

    # begin from the top-left corner:
    t.up()
    fp = rounded_point(first)
    t.goto(fp[0], fp[1])
    t.down()
    t.begin_fill()

    # reposition the turtle pen to complete the square:
    for p in points:
        rp = rounded_point(p)
        t.goto(rp[0], rp[1])
    t.end_fill()


# draw all the squares:
[draw_square(index, square) for index, square in enumerate(squares)]
turtle.done()
