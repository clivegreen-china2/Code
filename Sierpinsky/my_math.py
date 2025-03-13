# make type hinting simpler:
from typing import Tuple
type point = Tuple[float, float]
type square = Tuple[point, point, point, point]


def rounded_point(p: point) -> tuple[int, int]:
    """
    Rounds floating point coordinates to the nearest integers
    :param p: a tuple of x and y ordinates as floats
    :return: a tuple of x and y ordinates as ints
    """
    return round(p[0]), round(p[1])


def power_of_two(power: float) -> float:
    """
    Raises 2 to the power (exponent) supplied
    and returns a floating point result.
    """
    return pow(2.0, power)


def mid_point(start: point, end: point) -> point:
    """
    Returns a point halfway between the two points
    provided.
    :param start: a start location
    :param end: an end location
    :return: the half-way point
    """
    sx, sy = start[0], start[1]
    ex, ey = end[0], end[1]
    mx, my = (sx+ex)/2.0, (sy+ey)/2.0
    return mx, my,
