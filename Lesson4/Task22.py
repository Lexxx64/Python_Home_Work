list_1 = list(map(int, input('Введите числа через пробел: ').split()))
list_2 = list(map(int, input('Введите числа через пробел: ').split()))
print(sorted(set(list_1) & set(list_2)))

