# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3 Output: [4, 5, 1, 2, 3]

k = 3
lst = [1, 2, 3, 4, 5]
# new_lst = lst[k:] + lst[:k]
# print(new_lst)

# for i in range(k):
#     for j in range(len(lst) - 1):
#         temp = lst[j]
#         lst[j] = lst[j + 1]
#         lst[j + 1] = temp
# print(lst)        

for i in range(k - 1):
    last_el = lst.pop()
    lst.insert(0, last_el)
print(lst)