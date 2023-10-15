# from sys import argv
# script_name, first_param, ...
# print('Имя скрипта: ', script_name)


# from functools import reduce
# def my_func(prev_el, el):
#     print(f'{prev_el}, {el}')
#     return prev_el + el

# print(reduce(my_func, (10, 20, 30, 40))) # -> 60


from itertools import count
for el in count(7, 2):        # начиная с 7, шаг2
    if el > 15:               # до 15
        break
    else:
        print(el)