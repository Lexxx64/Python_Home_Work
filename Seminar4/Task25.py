list = input('Введите символы:\n').split()
result = []

for i in list:
    result.append(i)
    if result.count(i) == 1:
        print(i, end=' ')
    else:
        print(f'{i}_{result.count(i)-1}', end=' ')
    # if i in result:
    #     print(f'{i}_{result[i]}', end=' ')
    # else:
    #     print(i, end=' ')
    # result[i] = result.get(i, 0) + 1
