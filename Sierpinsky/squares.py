from my_math import *


# what is the size of the smallest square we will use?
min_size_exp: int = 3
min_size: float = power_of_two(min_size_exp)  # i.e.: 3 => a side length of 8.0

# where will we store each square's tuple of corner points?
squares: [square] = list()


def add_square(top_left: point, size: float) -> None:
    """
    Creates a collection of points defining a square.
    :param top_left: the point where the top left corner of the square is located
    :param size: the side length of the square
    """

    # ensure positive side length:
    size = abs(size)

    # calculate the corner points:
    tl: point = top_left
    tr: point = tl[0] + size, tl[1],  # top-right
    br: point = tl[0] + size, tl[1] - size,  # bottom-right
    bl: point = tl[0], tl[1] - size,  # bottom-left
    sq: square = tl, tr, br, bl,

    # store the completed square:
    squares.append(sq)

    # do we need to continue with quadrant squares?
    quad_size: float = size / 2.0
    if quad_size >= min_size:

        # top-right quadrant:
        add_square(mid_point(tl, tr), quad_size)

        # bottom-left quadrant:
        add_square(mid_point(tl, bl), quad_size)


def get_squares(start_size_exp: int) -> []:
    """
    Builds a list of squares.
    :param start_size_exp: a power of 2 that determines the size of the largest square
    :return: a list of tuples, each containing 4 corner points
    """
    # set size and position of starting square:
    start_size: float = power_of_two(start_size_exp)  # i.e.: 10 => 1024
    offset: float = start_size / 2.0
    start_at: point = -offset, offset,  # move centre of square to coordinate origin (0,0)

    # populate and return list of squares:
    add_square(start_at, start_size)
    return squares
