def my_func(x, y):
    try:
        x, y = int(x), int(y)
    except ValueError:
        return "Только числа"
    except ZeroDivisionError:
        return "y не должен быть равен 0"
    return round(x / y, 3)


print(my_func(input("ведите первое число: "), input("ведите второе число: ")))
