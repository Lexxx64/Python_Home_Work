Задача 34:

  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

*Пример:*

**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
    **Вывод:** Парам пам-пам  

    
Задача 36:

 На вход программы поступает строка в формате:

ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N

Необходимо с помощью функции map преобразовать ее в кортеж tp вида:

tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ..., ('ключ_N', 'значение_N'))

Выводить на экран получившийся кортеж.

Sample Input:

house=дом car=машина men=человек tree=дерево
Sample Output:

((house, дом), (car, машина), (men, человек), (tree, дерево))