def create_data():
    with open('Seminar8/data.txt', 'a', encoding='utf-8') as data:
        last_name = input('Введите фамилию: ').title()
        first_name = input('Имя: ').title()
        patronymic = input('Отчество: ').title()
        number = input('номер телефона: ')
        data.write(f'{last_name} {first_name} {patronymic} {number}\n')


def read_data():
    with open('Seminar8/data.txt', 'r', encoding='utf-8') as book:
        data = list(str(book.read()).split('\n'))
        return '\n'.join(data)


def search_user():
    with open('Seminar8/data.txt', 'r', encoding='utf-8') as book:
        data = list(str(book.read()).split('\n'))
        searching_data = input('Введите данные поиска: ')
        user = list()
        for el in data:
            if searching_data.lower() in el.lower():
                user.append(el)
        all_user = '\n'.join(user)
        print(all_user)


def change_user():
    with open('Seminar8/data.txt', 'a', encoding='utf-8') as book:
        data = list(str(book.read()).split('\n'))
        user = list()
        for i in range(len(user)):
            print(i)
