# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]
str_access='\n'.join(access_template)
str_trunk='\n'.join(trunk_template)

input_vlan_template={
    "access": 'Введите номер VLAN:',
    "trunk": 'Введите разрешенные VLANы:',
    }

mode_int={
    "access": str_access,
    "trunk": str_trunk,
    }

mode_1=input("Введите режим работы интерфейса (access/trunk): ") # access
type_1=input("Введите тип и номер интерфейса: ") #Fa0/6
num1=input(input_vlan_template[mode_1]) #3

print("Интерфейс: ", type_1)
print(mode_int[mode_1].format(num1))