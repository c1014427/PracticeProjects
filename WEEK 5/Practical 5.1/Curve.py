from Point import Point


class Curve():
    """Class to represent a list of points on a graph"""

    def __init__(self, *inputs):
        """constructor for a curve"""
        self.items = []
        for i in inputs:
            self.append_if_valid(i)

    def append_if_valid(self, item):
        """add a new point object to the curve"""
        if not isinstance(item, Point):
            raise TypeError("Curves only take point objects")
        self.items.append(item)

    def __str__(self):
        """string representation of a curve"""
        return "Curve:{}".format(self.items)

    def __repr__(self):
        """formal string representation of a curve"""
        s = ", "
        s = s.join([repr(x) for x in self.items])
        return "Curve({})".format(s)

    def __getitem__(self, index):
        """get point(s) in curve"""
        if isinstance(index, int):
            return self.items[index]
        else:
            return Curve(*self.items[index])

    def __setitem__(self, index, item):
        """update curve with given point value"""
        if not isinstance(item, Point):
            raise TypeError("Curves only take point objects")
        self.items[index] = item


# define a curve
cur = Curve(Point(1, 1), Point(2, 4), Point(3, 9))
# cur = Curve(Point(1,1),(2,2)) # should raise a TypeError
print(cur)
print(cur.__repr__())
# return a point/item
print(cur[1])  # == print(cur.__getitem__(1))
# return points/items i.e. subcurve
print(cur[0:2])  # == print(cur.__getitem__(0:2))
# update point
cur[1] = Point(1, 1)  # == print(cur.__setitem__(1,Point(1,1)))
# cur[1] = (1,1) # should raise a TypeError
print(cur)
