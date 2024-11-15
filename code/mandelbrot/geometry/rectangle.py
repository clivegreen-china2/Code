from geometry.point import Point


class Rectangle:

    def __init__(self,
                 center: Point = Point(0.0, 0.0),
                 width: float = 1.0,
                 height: float = 1.0
                 ):

        self.center, self.height, self.width = center, width, height

        self.left = self.center.x - self.width / 2
        self.top = self.center.y - self.height / 2
        self.right = self.left + self.width
        self.bottom = self.top + self.height

        self.top_left = Point(self.left, self.top)
        self.top_right = Point(self.right, self.top)
        self.bottom_left = Point(self.left, self.bottom)
        self.bottom_right = Point(self.right, self.bottom)
