# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки

def arithmetic_progression(first: int,
                           diff: int,
                           quantity: int) -> list[int]:

    list = [first + i * diff for i in range(quantity)]
    return list


print(arithmetic_progression(5, 10, 10))
