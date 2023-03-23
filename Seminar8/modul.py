import time
TXTFILE = 'Seminar8/data.txt'


def new_contact():
    last_name = input('Введите фамилию: ').title()
    first_name = input('Имя: ').title()
    patronymic = input('Отчество: ').title()
    number = input('номер телефона: ')
    contact = (f'{last_name} {first_name} {patronymic} {number}')
    return contact


def rec_contact():
    with open(TXTFILE, 'a', encoding='utf-8') as book:
        book.write(f'{new_contact()}\n')


def read_data():
    with open(TXTFILE, 'r', encoding='utf-8') as book:
        data = list(str(book.read()).split('\n'))
        for i, line in enumerate(data, start=1):
            if line.strip():
                print(i, line)


def search_user():
    with open(TXTFILE, 'r', encoding='utf-8') as book:
        data = list(str(book.read()).split('\n'))
        searching_data = input('Введите данные поиска: ')
        # user = list()
        for pos, el in enumerate(data):
            if searching_data.lower() in el.lower():
                print(pos, el)
        index = int(input('Введите соответствующий номер строки: '))
        action = input('Выберите действие:\n'
                       'd - удалить контакт\n'
                       'r - изменить контакт\n'
                       'o - я чисто посмотреть\n')
        if action == 'd':
            del data[index]
            print(f'Контакт {data[index]} удалён!')
            with open(TXTFILE, 'w', encoding='utf-8') as book:
                for line in data:
                    book.write(f'{str(line)}\n')
        time.sleep(1)
        if action == 'r':
            rename_contact = new_contact()
            print(f'Контакт {data[index]} изменён!')
            data[index] = rename_contact
            with open(TXTFILE, 'w', encoding='utf-8') as book:
                for line in data:
                    book.write(f'{str(line)}\n')
        time.sleep(1)


def ren_del_user():
    print(search_user())
    pass
