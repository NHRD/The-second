class Compare:

    def __init__(self, obj1, obj2):
        self.object1 = obj1
        self.object2 = obj2

    def compare(self):
        return self.object1 is self.object2

obj1 = input("Input something:")
obj2 = input("Input something:")
    
result = Compare(obj1, obj2).compare()

print(result)
