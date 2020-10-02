from abc import ABC, abstractmethod


class Cloth(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def get_square(self):
        pass

    def __add__(self, other):
        return self.get_square + other.get_square


class Coat(Cloth):
    @property
    def get_square(self):
        print(f'Ткани на пальто {round(self.param / 6.5 + 0.5)}')
        return round(self.param / 6.5 + 0.5)


class Jacket(Cloth):
    @property
    def get_square(self):
        print(f'Ткани на костюм {round(self.param * 2 + 0.3)}')
        return round(self.param * 2 + 0.3)


coat = Coat(58)
jacket = Jacket(18)

print(coat + jacket)
