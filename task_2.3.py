number = int(input("Введите порядковый номер месяца: "))
if 12 >= number >= 1:
    month_dict = {1: 'Январь',
                  2: 'Февраль',
                  3: 'Март',
                  4: 'Апрель',
                  5: 'Май',
                  6: 'Июнь',
                  7: 'Июль',
                  8: 'Август',
                  9: 'Сентябрь',
                  10: 'Октябрь',
                  11: 'Ноябрь',
                  12: 'Декабрь'}
    month_list = list(month_dict.values())
    for i, el in enumerate(month_list):
        if i == number-1:
            print(f"Месяц по списку {month_list[i]}")
            break
    print(f"Месяц по списку {month_dict[number]}")
else:
    print("Ошибка ввода")