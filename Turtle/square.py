from typing import Tuple
from shape import draw_square
import turtle
type pen = turtle.Turtle
type vertex = Tuple[int, int]


# set up the canvas area to draw onto:
turtle.setup(800, 800)
window = turtle.Screen()
window.bgcolor("black")
window.title("Square")

# set up the pen we will draw with:
my_pen: pen = turtle.Turtle()
my_pen.speed(0)
my_pen.hideturtle()

# specify square position, size and colour:
top_left: vertex = -300, 300,
side_length: int = 600
color: str = 'blue'

# draw a single square:
draw_square(my_pen, top_left, side_length, color)

# draw another one on top of it:
diff: int = 20
new_top_left: vertex = (
    top_left[0] + diff,
    top_left[1] - diff
)
new_side_length: int = side_length - diff * 2
new_color: str = 'yellow'

draw_square(
    my_pen,
    new_top_left,
    new_side_length,
    new_color
)

# tell turtle when we have finished:
turtle.done()
