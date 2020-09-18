def func(x, y):
    try:
        x, y = float(x), int(y)
        return 1 / x ** abs(y)
    except TypeError:
        return "Error"

print(func(2, -3))
#print(func(input("Введите число: "), input("Введите второе число")))
