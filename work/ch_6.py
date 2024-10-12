# _*_ coding utf-8 _*_

username = input('Введите имя пользователя: ')
password = input('Введите пароль: ')

if len(password) < 3:
    print("Пароль короткий")
elif username in password:
    print('Пароль содержит имя пользователя')
else:
    print("Пароль для пользователя {} установлен".format(username))
