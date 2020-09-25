t_file = open('test.txt', 'w')
line = input('Введите текст \n')
while line:
    t_file.writelines(line + '\n')
    line = input('Введите текст ')
    if not line:
        break

t_file.close()
my_f = open('test.txt', 'r')
content = my_f.readlines()
print(content)
t_file.close()
