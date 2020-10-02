class Road:
    __length = None
    __width = None
    weight = None
    depth = None

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def mass(self):
        self.weight = 25
        self.depth = 5
        mass = self.length * self.width * self.weight * self.depth / 1000
        print(mass)


road_1 = Road(5000, 20)
road_1.mass()
