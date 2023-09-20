# Задача No5. Решение в группах
# Вагоны в электричке пронумерованы натуральными числами, начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда, а иногда – с «хвоста»;
# это зависит от того, в какую сторону едет электричка). В каждом вагоне написан его номер. Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j. 
# Он хочет определить, сколько всего вагонов в электричке. Напишите программу, которая будет это делать или сообщать, что без дополнительной информации это сделать невозможно.
# Input: 3 4(ввод на разных строках) Output: 6

# i = 3
# j = 4
# if i == j: 
#     print("Нужна дополнительная информация ")
# else:
#     print(i + j - 1)


i = int(input("Сколько вагонов прошел человек: "))
j = int(input("Номер текущего вагона: "))
if i == j:
    print("Недостаточно информации")
else:
    vagon = i + j - 1
    print(f"Количество вагонов {vagon}")    