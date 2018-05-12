class Shape:

    def __init__(self):
        pass
    
    def what_am_i(self):
        print("I am a shape.")

class Rectangle(Shape):

    def __init__(self):
        pass
        """self.side_length = l

    def calculate_perimeter(self):
        return self.side_length * 3"""

class Square(Shape):

    def __init__(self):
        pass

rectangle = Rectangle()
square = Square()
rectangle.what_am_i()
square.what_am_i()



         