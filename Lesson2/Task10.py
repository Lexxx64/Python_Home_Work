from random import randint

n = int(input('Введите количество монет: '))
avers = 0
revers = 0

for i in range(n):
    coin = randint(0, 1)
    print(coin)
    if coin == 0:
        avers += 1
    else:
        revers += 1
if avers > revers:
    print(revers)
else:
    print(avers)