from random import randint

n = int(input('Введите количество элементов массива: '))
list = [randint(1, 10) for i in range(n)]
num = list[0]
print(list)
x = int(input(' Ведите проверяемое число: '))

for i in list:
    if (i - x) < (num - x):
        num = i
print(list)
print(f'{x}\n=> {num}')
