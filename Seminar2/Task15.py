# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

from random import randint
n = int(input('Введите количество арбузов: '))
max_watermelon = 0
min_watermelon = 30000

for i in range(n):
    watermelon = randint(3,20)
    print(watermelon)
    if watermelon > max_watermelon:
        max_watermelon = watermelon
    
    if watermelon < min_watermelon:
        min_watermelon = watermelon
print(min_watermelon, max_watermelon)