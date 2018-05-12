class Triangle:

    def __init__(self, b, h):
        self.base = b
        self.hight = h

    def area(self):
       areasize = (self.base * self.hight) / 2
       return areasize

base = float(input("Base length: "))
height = float(input("Height: "))
area = Triangle(base, height)
print("Area size is {}.".format(area.area()))
