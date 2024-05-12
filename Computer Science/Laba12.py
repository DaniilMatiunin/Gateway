'''Решите задачу о количестве способов достичь точки n из точки 1,
 если кузнечик умеет прыгать +1, +2 и *3.'''
def supergrasshopper(n):
    sg = [None] + ([0] * max(3, n))
    sg[1] = 1
    sg[2] = 1
    for i in range(3, n + 1):
        sg[i] = sg[i - 1] + sg[i - 2]
        if i % 3 == 0:
            sg[i] += sg[i // 3]
    return sg[n]
n=int(input('Введите конечную точку: '))
print('Количество способов добраться до  неё:',supergrasshopper(n))

'''Рассмотрим задачу для двух данных строк найти такую строку наибольшей длины, которая была бы 
подпоследовательностью каждой из них. Например, если A='abcabaac', B='baccbca' то у строк A и B них есть 
общая подпоследовательность длины 4, например, 'acba' или 'acbc'
Напишите программу решающую данную задачу с помощью алгоритма, полученного на основе
 динамического программирования..'''
import numpy as np
def maxisequence(line1, line2):
    line1.insert(0, '1')
    line2.insert(0, '2')
    Mse1 = np.zeros((len(line1) + 1, len(line2) + 1))
    Mse2 = np.zeros((len(line1) + 1, len(line2) + 1))
    for i in range(1, len(line2) + 1):
        for j in range(1, len(line1) + 1):
            if line1[j - 1] == line2[i - 1]:
                Mse1[j][i] = 1 + Mse1[j - 1][i - 1]
                Mse2[j][i] = -1
            else:
                if Mse1[j - 1][i] >= Mse1[j][i - 1]:
                    Mse1[j][i] = Mse1[j - 1][i ]
                    Mse2[j][i] = 2
                else:
                    Mse1[j][i] = Mse1[j][i - 1]
                    Mse2[j][i] = 1

    j = len(line1)
    i = len(line2)
    sequences = []
    sequence1 = ''
    while Mse2[j][i] != 0:
        if Mse2[j][i] == -1:
            sequence1 += line1[j - 1]
            j -= 1
            i -= 1
        elif Mse2[j][i] == 1:
            if sequence1 != '':
                sequences.append(sequence1)
                sequence1 = ''
            i -= 1
        elif Mse2[j][i] == 2:
            if sequence1 != '':
                sequences.append(sequence1)
                sequence1 = ''
            j -= 1
    if len(sequences) == 0:
        return
    else:
        mas = 0

        for i in range(1, len(sequences)):
            if len(sequences[mas]) < len(sequences[j]):
                mas = j
        alle = list(sequences[mas])
        alle.reverse()
        alle= ''.join(alle)
        return alle


line1=list(str(input('Введите  последовательность 1 ')))
line2=list(str(input('Введите  последовательность 2  ')))

print(maxisequence(line1,line2))
'''Даны две последовательности целых чисел 
Выяснить, является ли вторая последовательность подпоследовательностью первой, то есть можно ли из
 первой вычеркнуть некоторые члены так, чтобы осталась вторая.'''
def subsequence(line1, line2):
    x, y = 0, 0
    j = 0
    i = 0
    while i < len(line1):
        if line1[i] == line2[j]:
            y = i
            x += 1
            i += 1
            if j < len(line2) - 1:
                j += 1
            elif x < len(line2):
                return False
        else:
            i += 1
        if x == len(line2):
            return True
    return False
line1=str(input('Введите первую последовательность: '))
line2=str(input('Введите вторую последовательность: '))
print(subsequence(line1,line2))
'''На вершине лесенки, содержащей N ступенек, находится мячик, который начинает прыгать по ним вниз, 
к основанию. Сначала мячик может прыгнуть максимум на N/2, но с каждым ударом о ступеньку эта величина
 сокращается вдвое пока он не начинает катиться, перекатываясь с одной ступеньке на другую. 
 Так мячик может прокатиться ещё N/16 ступенек.

Определите число всевозможных "маршрутов" мячика и найдите максимально возможную длину лестницы N.'''

def ballj(init, n, step, show = False):
    if init >= n:
        return 0
    if n // 2 ** step < 1:
        return min(n // 16, n - init)
    routes = min(n // 2 ** step, n - init)
    for i in range(init + 1, min(init + n // 2 ** step, n) + 1):
        if show: print(init, '->', i)
        routes += ballj(i, n, step + 1, show)
    return routes

ballj(1, 4, 1, show = True)

print(ballj(1, int(input('Введите n: ')), 1, show = (True if input('Показывать все возможные ходы? (y/n) ') == 'y' else False)))
'''При испотльзовании динамического программирования поскольку мы ищем маршрут, естественной
 подзадачей является нахождение начальной части маршрута. Предположим, мы вышли из города 1,
  посетили несколько городов и сейчас находимся в городе j. Существенной информацией об этом
   частичном маршруте является где мы находимся (j), а также где мы уже побывали (чтобы не идти туда 
   второй раз).
 Это и приводит нас к необходимой подзадаче.'''
