def create_data():
    with open('Seminar8/data.txt', 'a', encoding='utf-8') as data:
        data.write(f'{input("Введите данные нового абонента: ")}\n')


def read_data():
    with open('Seminar8/data.txt', 'r', encoding='utf-8') as f:
        data = list(str(f.read()).split('\n'))
    return data


def search_user(book, searching_data):
    for el in book:
        if searching_data.lower() in el.lower():
            return el
    return -1


print('режимы работы\n 1 - запись\n 2 - поиск\n 0 - выход')


while True:
    mode = input('Выбор режима работы: ')
    if mode == '1':
        create_data()
    elif mode == '2':
        print(search_user(read_data(), input('Введите данные для поиска: ')))
    elif mode == '0':
        break
    else:
        print('Неверное значение')
