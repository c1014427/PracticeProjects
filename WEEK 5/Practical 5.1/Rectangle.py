from Point import Point


class Rectangle:
    """class to represent a rectangle on a graph"""

    def __init__(self, o, w, l):
        """constructor for a rectangle, origin point is the middle"""
        if not isinstance(o, Point):
            raise TypeError("Origin should be a Point object")
        self.origin = o
        self.width = w
        self.length = l

    def __str__(self):
        """string representation of a rectangle"""
        return "Rectangle({},{},{},{})".format(self.origin.x, self.origin.y,
                                               self.width, self.length)

    def __repr__(self):
        """formal string representation of a rectangle"""
        return "Rectangle({},{},{})".format(self.origin, self.width, self.length)

    def area(self):
        """method to find area of a rectangle"""
        area = self.width * self.length
        return area

    def perimeter(self):
        """method to find perimeter of a rectangle"""
        perimeter = (self.width + self.length) * 2
        return perimeter

    def __contains__(self, p):
        """method to determine whether a given point is inside the object"""
        # check x value is valid
        if p.x < self.origin.x - self.width / 2 or p.x > self.origin.x + self.width / 2:
            return False
        # check if y value is valid
        if p.y < self.origin.y - self.length / 2 or p.y > self.origin.y + self.length / 2:
            return False
        return True


# define a rectangle
r = Rectangle(Point(1, 1), 2, 3)
# r = Rectangle((1,1),2,3) # should raise a TypeError
print(r)
print(r.__repr__())
print("{} -> area={}, peri={}".format(r, r.area(), r.perimeter()))
# should be true
print(Point(1, 1) in r)  # == print(r.__contains__(Point(1,1)))
print(Point(1, 0) in r)
# should be false
print(Point(0, 3) in r)
print(Point(3, 0) in r)
