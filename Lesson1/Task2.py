# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

num = input('Введите трёхзначное число: ')
num = int(num)

if num < 100 or num > 999:
    print('Это не трёхзначное число')
else:
    d1 = num % 10
    d2 = num % 100 // 10
    d3 = num // 100
    print('Сумма цифр трёхзначного числа: ', d1 + d2 + d3)






