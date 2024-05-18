'''Найдите в числе π
 номер цифры в дробной части после которой идёт последовательность из:
шести 9;
шесть 8;
шесть 0;
первых шести цифр;
семь цифр вашего номера телефона.'''
from sympy import *
import numpy as np
import time
import pylab
import matplotlib.pyplot as plt


npi=2024518

PI = [str(i) for i in str(pi.n(npi))[2:]]

def finding9(n):
    f=''.join(n)
    s=f.find('999999')

    print('Нужная нам последовательность 9 находится на позиции :',s+1)

start_time = time.time()
PI1 = finding9(PI)
Tame1=time.time()-start_time
def finding8(s):

    mx = 1
    cnt = 1
    acht = []
    for i in range(len(s) - 1):
        if s[i] == '8' and s[i + 1] == '8':
            cnt += 1
            if cnt == 2:
                acht.append(i)
            if cnt == 6:
                break
        else:
            cnt = 1
    print(max(acht) + 1)

def finding0(s):

    mx = 1
    cnt = 1
    zero = []
    for i in range(len(s) - 1):
        if s[i] == '0' and s[i + 1] == '0':
            cnt += 1
            if cnt == 2:
                zero.append(i)
            if cnt == 6:
                break
        else:
            cnt = 1
    print(max(zero) + 1)

def findingnumber(n):
    f = ''.join(n)
    s = f.find('4277415')

    print('Нужная нам последовательность 9 находится на позиции :', s + 1)

def findingfirst(n):
    f = ''.join(n)
    s = f.find('141592')

    print('Нужная нам последовательность 9 находится на позиции :', s + 1)


start_time = time.time()
PI2 = finding8(PI)
Tame2=time.time()-start_time

start_time = time.time()
PI3 = finding0(PI)
Tame3=time.time()-start_time

start_time = time.time()
PI4 = finding0(PI)
Tame4=time.time()-start_time

start_time = time.time()
PI5 = findingfirst(PI)
Tame5=time.time()-start_time

#ЗАДАНИЕ 2
'''Реализуйте алгоритмы сужения области:
бинарный поиск
метод золотого сечения
интерполирующи й поиск'''
#БИНАРНЫЙ ПОИСК
from random import randint

a = [randint(1, 50) for i in range(10)]
a.sort()
print(a)

value = int(input('введите число для поиска его номера '))

def BinarySearch(a,value):
	left = 0
	right = len(a) - 1
	center = (left + right) // 2

	while a[center] != value:
		if value > a[center]:
			left = center + 1
		else:
			right = center - 1
		center = (left + right) // 2
		if left >= right:
			break

	if value == a[center]:
		print('индекс элемента', center)
	else:
		print('нет искомого')

start_time = time.time()
Bs = BinarySearch(a,value)
TameB=time.time()-start_time

#метод золотого сечения
def func(x):
    return x**2
def golden_section(func, a, b, tol=1e-5):
    phi = (1 + 5**0.5) / 2
    c = b - (b - a) / phi
    d = a + (b - a) / phi
    while abs(c - d) > tol:
        if func(c) < func(d):
            b = d
        else:
            a = c

        c = b - (b - a) / phi
        d = a + (b - a) / phi
    return (a + b) / 2


start_time = time.time()
GsS = golden_section(func(),0,4)
TameGsS=time.time()-start_time
#интерполирующий поиск
def interpolationSearch(arr, lo, hi, x):


    if (lo <= hi and x >= arr[lo] and x <= arr[hi]):

        pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) *
                    (x - arr[lo]))


        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            return interpolationSearch(arr, pos + 1,
                                    hi, x)
        if arr[pos] > x:
            return interpolationSearch(arr, lo,
                                    pos - 1, x)
    return -1


arr = [14, 12, 13, 16, 18, 19, 20,
    21, 22, 23, 24, 33, 35, 42, 47]
n = len(arr)
print(arr)
x = 22
start_time = time.time()
index = interpolationSearch(arr, 0, n - 1, x)
TameIndex=time.time()-start_time

if index != -1:
    print("Индекс числа:", index)
else:
    print("число не найдено")

'''Сравните производительность алгоритмов из задания 2 на задании 1.'''

print(f'время выполнения 1 задания : {Tame1}')
print(f'время выполнения 1 задания : {Tame2}')
print(f'время выполнения 1 задания : {Tame3}')
print(f'время выполнения 1 задания : {Tame4}')
print(f'время выполнения 1 задания : {Tame5}')
print(f'время выполнения 2 задания : {TameB}')
print(f'время выполнения 2 задания : {TameGsS}')
print(f'время выполнения 2 задания : {TameIndex}')