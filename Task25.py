# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

mas = input("Введите символы через пробел: ").split(" ")
# my_dict = dict()
# for item in mas:
#     if item in my_dict:
#         print(f"{item}_{my_dict[item]}", end = ' ')
#     else:
#         print(item, end = ' ')

# my_dict[item] = my_dict.get(item, 0) + 1

res = {}
for el in mas:
    if el in res:
        print(f"{el}_{res[el]}", end = " ")
    else:
        print(el, end = " ")
    res[el] = res.get(el, 0) + 1