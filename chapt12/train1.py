class Apple:
    def __init__(self, w, c, t, k):
        self.weight = w
        self.color = c
        self.taste = t
        self.kind = k
        print("Created!")

apple = Apple("50", "Red", "Bad", "Fuji")
print(apple.color)
print(apple.kind)
