import math

from Point import Point


class Circle():
    """Class to represent a circle on a graph"""

    def __init__(self, o, r):
        """constructor for a circle, origin point is middle"""
        if not isinstance(o, Point):
            raise TypeError("Origin should be a Point object")
        self.o = o
        self.r = r

    def __str__(self):
        """string representation of a circle"""
        return "Circle({},{},{})".format(self.o.x, self.o.y, self.r)

    def __repr__(self):
        """formal string representation of a circle"""
        return "Circle({},{})".format(self.o, self.r)

    def area(self):
        """method to find the area of a circle"""
        return math.pi * self.r ** 2

    def perimeter(self):
        """method to find the perimeter of a circle"""
        return 2 * math.pi * self.r

    def __contains__(self, p):
        """method to determine whether a given point is inside the object"""
        # Adapted from
        # https://www.geeksforgeeks.org/find-if-a-point-lies-inside-or-on-circle/
        return ((p.x - self.o.x) ** 2 + (p.y - self.o.y) ** 2) <= (self.r ** 2)


# define a circle
cir = Circle(Point(1, 1), 2)
# c = Circle((1,1),2) # should raise a TypeError
print(cir)
print(cir.__repr__())
print("{} -> area={}, peri={}".format(cir, cir.area(), cir.perimeter()))
# should be true
print(Point(1, 1) in cir)  # == print(cir.__contains__(Point(1,1)))
print(Point(1, 0) in cir)
# should be false
print(Point(0, 3) in cir)
print(Point(3, 0) in cir)
