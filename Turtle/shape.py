from typing import Tuple, List
import turtle
type vertex = Tuple[int, int]
type vertices = List[vertex]
type pen = turtle.Turtle


def draw_filled_shape(
        my_pen: pen,
        my_vertices: vertices,
        my_color: str = 'red'
) -> None:

    my_pen.fillcolor(my_color)

    # move the first point from the start to the end:
    first_vertex: vertex = my_vertices.pop()
    my_vertices.append(first_vertex)

    # move to the first point and get ready to draw:
    my_pen.up()
    x: int = first_vertex[0]
    y: int = first_vertex[1]
    my_pen.goto(x, y)
    my_pen.down()
    my_pen.begin_fill()

    # move the turtle pen to each point in turn,
    # to draw out the shape:
    for p in my_vertices:
        x, y = p[0], p[1]
        my_pen.goto(x, y)

    # we turn off the fill when finished:
    my_pen.end_fill()


def draw_square(
        t: pen,
        top_left:
        vertex, side_length: int,
        color: str
) -> None:

    top_right: vertex = (
        top_left[0] + side_length,
        top_left[1]
    )
    bottom_right: vertex = (
        top_left[0] + side_length,
        top_left[1] - side_length
    )
    bottom_left: vertex = (
        top_left[0],
        top_left[1] - side_length
    )

    corners: vertices = [
        top_left,
        top_right,
        bottom_right,
        bottom_left
    ]
    draw_filled_shape(t, corners, color)
