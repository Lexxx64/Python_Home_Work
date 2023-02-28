from random import randint

n = int(input('Введите количество элементов массива: '))

list = [randint(1, 10) for i in range(n)]
print(list)
count = 0
x = int(input('Введите проверяемое число: '))
for i in range(n):
    if list[i] == x:
        count += 1
print(list)
print(f'{x}\n=> {count}')
