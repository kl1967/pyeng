# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
addr=input("Введите IP фдрес в формате 10.0.1.1: ")
#print(addr)
#print(type(addr))

l_addr = addr.split('.')
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
#'''