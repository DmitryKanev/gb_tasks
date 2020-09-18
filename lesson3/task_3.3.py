# def my_func(num1, num2, num3):
#    list = [num1, num2, num3]
#    try:
#        list.pop(list.index(min(list)))
#        return sum(list)
#    except TypeError:
#        return "Вводите только числа"


#print(my_func(15, 24, 2))


def my_func(num1, num2, num3):
    list = [num1, num2, num3]
    min_1 = min(list)
    list.remove(min_1)
    return sum(list)

print(my_func(15, 24, 2))
