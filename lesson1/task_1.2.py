i = int(input("Введите количество секунд: "))
hours = i // 3600
minutes = (i - hours * 3600) // 60
seconds = i - (hours * 3600 + minutes * 60)
print(f"Время в формате чч:мм:сс  {hours}:{minutes}:{seconds}")


