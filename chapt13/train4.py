class Horse:

    def __init__(self, name, rider):
        self.name = name
        self.rider = rider
    
    def change_rider(self, name):
        self.name = name

class Rider:

    def __init__(self, name):
        self.name = name

ankatsu = Rider("Katsumi Ando")
daiwa = Horse("Daiwa major", ankatsu)

print(daiwa.rider.name)






         