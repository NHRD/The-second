class Square:
    
    square_list = []

    def __init__(self, len, wid, high):

        self.length = len
        self.width = wid
        self.hight = high
        self.square_list.append([self.length, self.width, self.hight])
    
    def __repr__(self):
        return "{} by {} by {} by {}".format(self.length, self.width,
        self. hight, self.hight)
    
print(Square.square_list)

s1 = Square(1, 1, 1)
s2 = Square(2, 2, 2)
s3 = Square(5, 1, 6)

print(s1)
print(s2)
print(s3)
print(Square.square_list)