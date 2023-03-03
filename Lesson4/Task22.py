list_1 = list(map(int, input('Введите числа через пробел: ').split()))
list_2 = list(map(int, input('Введите числа через пробел: ').split()))
new_list = set()

for i in list_1:
    if i in list_2:
        new_list.add(i)
print(sorted(new_list))
