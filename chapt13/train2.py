class Rectangle:

    def __init__(self,l):
        self.side_length = l

    def calculate_perimeter(self):
        return self.side_length * 3

class Square:

    def __init__(self,l):
         self.side_length = l

    def calculate_perimeter(self):
        return self.side_length * 4
    
    def change_size(self,l2):
        self.side_length = self.side_length + l2

rectangle_peri = Rectangle(1)
square_peri = Square(1)
length1 = square_peri.side_length
print(rectangle_peri.calculate_perimeter(),
square_peri.calculate_perimeter())
square_peri.change_size(1)
print("Side length of square has changed from {} to {}.".format(length1,
 square_peri.side_length))
print(square_peri.calculate_perimeter())


         