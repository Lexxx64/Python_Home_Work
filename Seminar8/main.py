from modul import *

print('режимы работы\n'
      '1 - создать новый контакт\n'
      '2 - найти контакт\n'
      '3 - изменить или удалить контакт\n'
      '4 - просмотр телефонной книги\n'
      '5 - нумератор\n'
      '0 - выход')


while True:
    mode = input('Выбор режима работы: ')
    if mode == '1':
        create_data()
    elif mode == '2':
        search_user()
    elif mode == '3':
        print(ren_del_user())
    elif mode == '4':
        print(read_data())
    elif mode == '5':
        print(numerate())
    elif mode == '0':
        break
    else:
        print('Неверное значение')
