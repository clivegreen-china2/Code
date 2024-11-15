

class Line:

    def __init__(self,
                 point_a: Point = Point(0.0, 0.0),
                 point_b: Point = Point(0.0, 0.0)
                 ):
        self.point_A, self.point_B = point_a, point_b

    def length(self):
        w = abs(self.point_B.x - self.point_A.x)
        h = abs(self.point_B.y - self.point_A.y)
        return (w**2 + h**2)**0.5  # Pythagoras
