from itertools import count
from itertools import cycle

my_list = []
my_list_2 = []

for el in count(14, 24):
    if el > 255:
        break
    else:
        my_list.append(chr(el))

a = 0
for el in cycle(my_list):
    if a > 5:
        break
    my_list_2.append(ord(el))
    a += 1

print(my_list)
print(my_list_2)
