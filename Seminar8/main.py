from modul import * # noqa


while True:
    print('режимы работы\n'
          '1 - создать новый контакт\n'
          '2 - найти, изменить, удалить контакт\n'
          '3 - просмотр телефонной книги\n'
          '0 - выход')
    mode = input('Выбор режима работы: ')
    if mode == '1':
        rec_contact() # noqa
    elif mode == '2':
        search_user() # noqa
    elif mode == '3':
        read_data() # noqa
    elif mode == '0':
        break
    else:
        print('Неверное значение')
