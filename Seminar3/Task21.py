# 21. Напишите программу для печати всех уникальных значений в словаре.
# {  1:2, 3:4 , 2:2  } -> 4,2

dictionary = {1: 2, 3: 4, 2: 2}
set_1 = set()
for item in dictionary:
    set_1.add(dictionary[item])
print(*set_1)
