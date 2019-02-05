class Circle:
    def __init__(self, radius_):
        self.radius = radius_
        return radius_

    def area_(self):
        area = 3.14 * self.radius * self.radius
        return area

    def perimeter_(self):
        perimeter = 2 * 3.14 * self.radius
        return perimeter


c = Circle(2)
c.area_()
c.perimeter_()