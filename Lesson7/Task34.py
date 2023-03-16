def winnie_puh_rap(rap):
    poem = rap.lower().split()
    phrase = list(map(lambda x: sum(i in 'аеёийоуыэюя' for i in x), poem))
    if len(set(phrase)) == 1:
        return 'Парам пам-пам'
    return 'Пара-пам'


rap = input('Введите текст стиха: ')
print(winnie_puh_rap(rap))
