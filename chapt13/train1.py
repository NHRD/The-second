class Rectangle:

    def __init__(self,l):
        self.side_length = l
    def calculate_perimeter(self):
        return self.side_length *3

class Square:

    def __init__(self,l):
         self.side_length = l
    def calculate_perimeter(self):
        return self.side_length *4

rectangle_peri = Rectangle(1)
square_peri = Square(1)
print(rectangle_peri.calculate_perimeter(),
square_peri.calculate_perimeter())

         