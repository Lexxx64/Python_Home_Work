import math
s = int(input('Введите сумму чисел: '))
p = int(input('Введите произведение чисел: '))
print(s)
print(p)
x = int((s - math.sqrt(s**2-4*p))/2)
y = int(s - x)
print(x, y)
