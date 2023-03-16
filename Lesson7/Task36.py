lst_1 = input('Введите данные').split()
lst_2 = tuple(map(lambda x: tuple(x.split('=')), lst_1))
print(lst_2)
