import Point


def main():
    # define a point
    # p = Point.Point(2, 1)
    p = Point.Point('2', 1)  # should raise a TypeError
    print(p)  # == print(p.__str__())
    print(p.__repr__())


main()
