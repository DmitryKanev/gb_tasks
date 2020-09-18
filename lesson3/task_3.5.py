def summ():
    result = 0
    while True:
        numbs = input("Вводите числа через пробел или q чтобы выйти: ").split()
        for num in numbs:
            if num == "q":
                return result
            else:
                try:
                    result += int(num)
                except ValueError:
                    print("Чтобы выйти из программы введите  'q'.")
        print(f"Сумма чисел равна {result}")


print(summ())
