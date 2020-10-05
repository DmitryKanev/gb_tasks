class Error:
    def __init__(self, *args):
        self.my_list = []

    def num_input(self):

        while True:
            try:
                num = int(input('Введите значения и нажимайте Enter - '))
                self.my_list.append(num)
                print(f'Прошли проверку {self.my_list} \n ')
            except:
                print(f"Недопустимое значение ")
                y_or_n = input(f'Попробовать еще раз? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.num_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'Вы вышли'
                else:
                    return f'Вы вышли'


try_except = Error(4)
print(try_except.num_input())
