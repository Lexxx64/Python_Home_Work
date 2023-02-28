import re


def language_ru(text):
    return bool(re.search('[а-яА-Я]', text))


price_eng = {1: 'AEIOULNSTR',
             2: 'DG',
             3: 'BCMP',
             4: 'FHVWY',
             5: 'K',
             8: 'JX',
             10: 'QZ'}
price_ru = {1: 'АВЕИНОРСТ',
            2: 'ДКЛМПУ',
            3: 'БГЁЬЯ',
            4: 'ЙЫ',
            5: 'ЖЗХЦЧ',
            8: 'ШЭЮ',
            10: 'ФЩЪ'}

text = input('Введите текст: ').upper()

if language_ru(text):
    print(sum(k for i in text for k, v in price_ru.items() if i in v))
else:
    print(sum(k for i in text for k, v in price_eng.items() if i in v))
