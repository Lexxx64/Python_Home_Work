def create_data():
    with open('Seminar8/data.txt', 'r+', encoding='utf-8') as book:
        data = list(str(book.read()).split('\n'))
        last_name = input('Введите фамилию: ').title()
        first_name = input('Имя: ').title()
        patronymic = input('Отчество: ').title()
        number = input('номер телефона: ')
        for el in data:
            if number in el:
                return print('Такой номер существует')
        book.write(f'{last_name} {first_name} {patronymic} {number}\n')


def read_data():
    with open('Seminar8/data.txt', 'r', encoding='utf-8') as book:
        data = list(str(book.read()).split('\n'))
        return '\n'.join(data)


def numerate():
    with open('Seminar8/data.txt', 'r', encoding='utf-8') as book:
        for i, line in enumerate(book, start=1):
            print(i, line)


def search_user():
    with open('Seminar8/data.txt', 'r+', encoding='utf-8') as book:
        data = list(str(book.read()).split('\n'))
        searching_data = input('Введите данные поиска: ')
        # user = list()
        for pos, el in enumerate(data):
            if searching_data.lower() in el.lower():
                print(pos, el)
            return 'Такого пользователя нет'
        index = int(input('Введите соответсвующий номер строки: '))
        action = input('Выберите действие:\n'
                       'd - удалить контакт\n'
                       'r - изменить контакт\n'
                       'o - я чисто посмотреть\n')
        if action == 'd':
            del data[index]
            with open('Seminar8/data.txt', 'w', encoding='utf-8') as book:
                for line in data:
                    book.write(f'{str(line)}\n')
        # user.append(el)
        # choice = input('хотите изменитть контакт ')
        # if choice == 'y':
        #     return ren_del_user()
    # print('\n'.join(user))


def ren_del_user():
    print(search_user())

