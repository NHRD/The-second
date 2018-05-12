import math

class Circle:

    def __init__(self, di):
        self.diameter = float(di)

    def area(self):
        pi = math.pi
        return pi * (self.diameter) / 2 * (self.diameter) / 2

diameter = input("Input diameter: ")
area = Circle(diameter)
print("Area size is {}.".format(area.area()))
