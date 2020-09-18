from functools import reduce


def my_func(prev_el, el):
    return prev_el * el


even_l = [elem for elem in range(100, 1001) if elem % 2 == 0]

print(reduce(my_func, even_l))
