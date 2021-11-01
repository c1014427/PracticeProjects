class Point:
    """class to represent a point on a graph"""

    def __init__(self, x, y):
        """constructor for a point"""
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("Input values should be integers")
        self.x = x
        self.y = y

    def __str__(self):
        """string representation of a point"""
        return "Point({}, {})".format(self.x, self.y)

    def __repr__(self):
        """formal string representation of a point"""
        return "Point({}, {})".format(self.x, self.y)


def main():
    # define a point
    p = Point(2, 1)
    # p = Point('2', 1)  # should raise a TypeError
    print(p)  # == print(p.__str__())
    print(p.__repr__())


main()
