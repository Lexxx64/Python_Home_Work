from random import randint

number_of_beds = int(input('Введите количество грядок: '))
number_of_fruits = [randint(0, 10) for i in range(number_of_beds)]
print(number_of_fruits)
max_sum_blueberries = sum(number_of_fruits[:3])

for i in number_of_fruits:
    number_of_fruits.insert(0, number_of_fruits.pop())
    sum_sector_blueberries = sum(number_of_fruits[:3])
    if max_sum_blueberries < sum_sector_blueberries:
        max_sum_blueberries = sum_sector_blueberries
print(max_sum_blueberries)
