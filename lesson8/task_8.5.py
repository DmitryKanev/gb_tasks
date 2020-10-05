class MachineStore:
    my_store = []


class OfficeMachines:

    def __init__(self, name, price, quant):
        self.name = name
        self.price = price
        self.quant = quant

    def reception(self):
        try:
            i = int(input("Введите тип техники (1 для принтера, 2 для сканера, 3 для ксерокса) \n"))
            if i == 1:
                Printer.params(self)

            elif i == 2:
                Scanner.params_2(self)

            elif i == 3:
                Copier.params_3(self)

            else:
                print(f'Ошибка ввода')
        except ValueError:
            return f'Ошибка ввода'


class Printer(OfficeMachines):
    @staticmethod
    def params(self):
        unit = "Printer"
        unit_p = int(input(f'Введите цену за ед '))
        unit_q = int(input(f'Введите количество '))
        unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
        MachineStore.my_store.append(unique)
        print(MachineStore.my_store)
        return OfficeMachines.reception(self)


class Scanner(OfficeMachines):
    @staticmethod
    def params_2(self):
        unit = "Scanner"
        unit_p = int(input(f'Введите цену за ед '))
        unit_q = int(input(f'Введите количество '))
        unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
        MachineStore.my_store.append(unique)
        print(MachineStore.my_store)
        return OfficeMachines.reception(self)


class Copier(OfficeMachines):
    @staticmethod
    def params_3(self):
        unit = "Copier"
        unit_p = int(input(f'Введите цену за ед '))
        unit_q = int(input(f'Введите количество '))
        unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
        MachineStore.my_store.append(unique)
        print(MachineStore.my_store)
        return OfficeMachines.reception(self)


u_1 = 1
OfficeMachines.reception(u_1)
print(MachineStore.my_store)
