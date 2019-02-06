# from __future__ import print_function
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def length(self):
        print(self.a.x)
        print(self.b.x)
        print(self.a.y)
        print(self.b.y)
        return ((self.a.x - self.b.x) ** 2 + (self.a.y - self.b.y) ** 2) ** 0.5


p1 = Point(2, 3)
p2 = Point(5, 7)
l_ = Line(p1, p2)
print(l_.length())