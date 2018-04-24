#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Задание 4.1a

Всё, как в задании 4.1. Но, если пользователь ввел адрес хоста, а не адрес сети,
то надо адрес хоста преобразовать в адрес сети и вывести адрес сети и маску, как в задании 4.1.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.
"""

IP = input('Enter IP adress with mask(/): ')
BITMASK = int(IP.split('/')[1])
STRBITMASK=('1'*BITMASK+('0'*(32-BITMASK)))

print ('\n' + '-' * 41)
print ("Network:")

print ("{:<10} {:<10} {:<10} {:<10}\n{:10} {:10} {:10} {:10}".format(

int(('0'*(8-(len(bin(int(IP.split('.')[0]))[2:])))+bin(int(IP.split('.')[0]))[2:])[0:STRBITMASK[0:8].count('1')]+'0'*(8-STRBITMASK[0:8].count('1')),2),
int(('0'*(8-(len(bin(int(IP.split('.')[1]))[2:])))+bin(int(IP.split('.')[1]))[2:])[0:STRBITMASK[8:16].count('1')]+'0'*(8-STRBITMASK[8:16].count('1')),2),
int(('0'*(8-(len(bin(int(IP.split('.')[2]))[2:])))+bin(int(IP.split('.')[2]))[2:])[0:STRBITMASK[16:24].count('1')]+'0'*(8-STRBITMASK[16:24].count('1')),2),
int(('0'*(8-(len(bin(int(IP.split('/')[0].split('.')[3]))[2:])))+bin(int(IP.split('/')[0].split('.')[3]))[2:])[0:STRBITMASK[24:32].count('1')]+'0'*(8-STRBITMASK[24:32].count('1')),2),

('0'*(8-(len(bin(int(IP.split('.')[0]))[2:])))+bin(int(IP.split('.')[0]))[2:])[0:STRBITMASK[0:8].count('1')]+'0'*(8-STRBITMASK[0:8].count('1')),
('0'*(8-(len(bin(int(IP.split('.')[1]))[2:])))+bin(int(IP.split('.')[1]))[2:])[0:STRBITMASK[8:16].count('1')]+'0'*(8-STRBITMASK[8:16].count('1')),
('0'*(8-(len(bin(int(IP.split('.')[2]))[2:])))+bin(int(IP.split('.')[2]))[2:])[0:STRBITMASK[16:24].count('1')]+'0'*(8-STRBITMASK[16:24].count('1')),
('0'*(8-(len(bin(int(IP.split('/')[0].split('.')[3]))[2:])))+bin(int(IP.split('/')[0].split('.')[3]))[2:])[0:STRBITMASK[24:32].count('1')]+'0'*(8-STRBITMASK[24:32].count('1'))))

print ("Mask:")
print  ("/"+str(BITMASK))

print ("{:<10} {:<10} {:<10} {:<10}\n{:<10} {:<10} {:<10} {:<10}".format(
int(STRBITMASK[0:8],2),
int(STRBITMASK[8:16],2),
int(STRBITMASK[16:24],2),
int(STRBITMASK[24:32],2),

STRBITMASK[0:8],
STRBITMASK[8:16],
STRBITMASK[16:24],
STRBITMASK[24:32]))
