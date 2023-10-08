# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
# Input: 2 -> 3 4 Output: 4 3

# n = 3
# def func(n):
#     if n > 0:
#         el = int(input("Введите число: "))
#         func(n-1)
#         print(el, end=" ")
# func(n)

num = 1230
def reverse(num):
    if num < 10:
        return str(num)
    return str(num % 10) + reverse(num // 10)
print(reverse(num))