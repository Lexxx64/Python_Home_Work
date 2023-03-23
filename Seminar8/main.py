from modul import * # noqa


while True:
    print('режимы работы\n'
          '1 - создать новый контакт\n'
          '2 - найти контакт\n'
          '3 - изменить или удалить контакт\n'
          '4 - просмотр телефонной книги\n'
          '5 - нумератор\n'
          '0 - выход')
    mode = input('Выбор режима работы: ')
    if mode == '1':
        rec_contact() # noqa
    elif mode == '2':
        search_user() # noqa
    elif mode == '3':
        print(ren_del_user()) # noqa
    elif mode == '4':
        print(read_data()) # noqa
    elif mode == '5':
        print(numerate()) # noqa
    elif mode == '0':
        break
    else:
        print('Неверное значение')
