# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0 
# 2

n = int(input("Введите кол-во монет: "))
orel = reshka = 0
for i in range (n):
    x = int(input("Орел(1) или Решка(0) "))
    if x == 1:
        orel += 1
    else:
        reshka += 1
if orel < reshka:
    print(f"Переверните {orel} монет с орла на решку, их меньше всего")
elif orel == reshka:
    print(f"Кол-во орлов и решек одинаково, по {orel} штук")
else:
    print(f"Переверните {reshka} монет с решки на орла, их меньше всего") 

