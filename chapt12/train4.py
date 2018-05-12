class Hexagon:

    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.sides = [s1, s2, s3, s4, s5, s6]

    def perimeter(self):
        peri = 0
        for i in range(len(self.sides)):
            peri = peri + self.sides[i]
        return peri

result = Hexagon(1, 2, 3, 4, 5, 6)
result1 = result.perimeter()
print(result1)


