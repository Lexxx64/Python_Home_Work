# 17. Дан список чисел. Определите, сколько в нем встречается различных чисел.
# 1 2 3 1 2 4 -> 4 (1 2 3 4)

from random import randint
n = int(input("Введите кол-во чисел в списке  "))
list = [randint(-10, 10) for i in range(n)]
print(list)
result = set(list)
print(f'{len(result)}\n{result}')

