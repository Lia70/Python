# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6

array = [1, 1, 2, 0, -1, 3, 4, 4]
# print(len(set(array)))   

new_array = []
for el in array:
    if el not in new_array:
        new_array.append(el)
print(len(new_array))        

