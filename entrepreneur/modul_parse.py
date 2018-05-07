#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
R4>show cdp neighbors
вывод команды show cdp neighbors.
Например, если как аргумент был передан такой вывод:
Создать функцию parse_cdp_neighbors, которая обрабатывает
Функция должна возвращать словарь, который описывает соединения между устройствами.
Функция ожидает, как аргумент, вывод команды одной строкой.

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
	{('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
	 ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.
Ограничение: Все задания надо выполнять используя только пройденные темы.
Проверить работу функции на содержимом файла sw1_sh_cdp_neighbors.txt
'''
# from pprint import pprint
# inf=open('sh_cdp_n_sw1.txt')

def parse_cdp_neighbors(inf):
	'''
	inf - file, для которых необходимо сгенерировать конфигурацию, вида:
		{('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
		('R4', 'Fa0/2'): ('R6', 'Fa0/0')}
	'''
	result={}

	for line in inf:
		if '|' in line: # для ansible
			device=line.split(' |')[0]

		# if '#' in line: # для нормальной выгрузки
		# 	device=line.split('#')[0]
		# if '>' in line: # для нормальной выгрузки
		# 	device=line.split('>')[0]

		if not line.startswith('\n') and not line.startswith('Device ID') and not line.startswith('#') and not 'Shared' in line and not '|' in line and not ',' in line: # для анcибла
		# if not line.startswith('\n') and not line.startswith('Device ID') and not line.startswith('#') and not 'Shared' in line and not '>' in line and not ',' in line: # для выгрузки CDP
			list1=[device,(line.split()[1] + line.split()[2])]
			list2=[(line.split()[0]),(line.split()[-2] + line.split()[-1])]
			tuple1=tuple(list1)
			tuple2=tuple(list2)
			result[tuple1] = tuple2
	return result   

# pprint(parse_cdp_neighbors(inf))
# inf.closed