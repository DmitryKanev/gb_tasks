username = input('Введите имя пользователя: ')
original_pass = input('Задайте пароль: ')
password = input('Введите пароль: ')
access = False
if password == original_pass:
    print("Пароль принят. Здравствуйте," + username)
    access = True
else:
    print('Неправильный пароль.')