class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} начала движение'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'скорость {self.name} {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'скорость {self.name} {self.speed}')

        if self.speed > 40:
            return f'скорость {self.name} выше допустимой'
        else:
            return f'скорость {self.name} в пределах допустимого'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'скорость {self.name} {self.speed}')

        if self.speed > 60:
            return f'скорость {self.name} выше допустимой'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} полицейская'
        else:
            return f'{self.name} не полицейская'


audi = SportCar(100, 'Red', 'Audi', False)
oka = TownCar(30, 'Yellow', 'Oka', False)
lada = WorkCar(70, 'Green', 'Lada', True)
bmw = PoliceCar(110, 'Black', 'BMW', True)
print(lada.turn_left())
print(oka.turn_right())
print(lada.go())
print(lada.name)
print(audi.name)
print(f'{lada.name} полицейский автомобиль {lada.is_police}')
print(audi.show_speed())
print(oka.show_speed())
print(bmw.police())
print(bmw.show_speed())
