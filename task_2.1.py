my_int = 5
my_float = 1.2
my_str = "Hello world"
my_list = ['c', '4']
my_tuple = ('h', '5')
my_dict = {'city': 'St.Petersburg', 'country': 'Russia'}

super_list = [my_int, my_float, my_str, my_list, my_tuple, my_dict]
for i in super_list:
    print(f'{i} is {type(i)}')
