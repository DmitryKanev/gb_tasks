from time import sleep


class TrafficLight:
    __color = ['RED', 'YELLOW', 'GREEN']

    @staticmethod
    def running():
        i = 0
        while i < 3:
            print(f"Цвет светофора {TrafficLight.__color[i]}")
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(5)
            elif i == 3:
                break
            i += 1


tl_1: TrafficLight = TrafficLight()
tl_1.running()
