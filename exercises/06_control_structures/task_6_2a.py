# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
addr=input("Введите IP фдрес в формате 10.0.1.1: ")
#print(addr)
#print(type(addr))
l_addr = addr.split('.')
print(l_addr)
addr_true=True
if len(l_addr)==4:
    addr_true=True
else:
    addr_true=False

if addr_true:
    for dig in l_addr:
        if not dig.isdigit():
            addr_true=False
            break
if addr_true:
    for dig in l_addr:
        if int(dig)<0 and int(dig)>255:
            addr_true=False
            break
if not addr_true:
    print('Неправильный IP-адрес')

#print(l_addr)

if int(l_addr[0]) >= 1 and int(l_addr[0])<=223:
    print('unicast')
elif int(l_addr[0]) >= 4 and int(l_addr[0])<=239:
    print('multicast')
elif int(l_addr[0]) == 255 and int(l_addr[1])==255 and int(l_addr[2]) == 255 and int(l_addr[3])==255:
    print('local broadcast')
elif int(l_addr[0]) == 0 and int(l_addr[1])==0 and int(l_addr[2]) == 0 and int(l_addr[3])==0:
    print('unassigned')
else:
    print('unused')