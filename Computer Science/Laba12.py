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
def maxsequence(line1,line2):
    n = len(line1)
    m = len(line2)
    qwa = [[0] * (m + 1) for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if line1[i - 1] == line2[j - 1]:
                qwa[i][j] = qwa[i - 1][j - 1] + 1
            else:
                qwa[i][j] = max(qwa[i - 1][j], qwa[i][j - 1])
    tot = []
    i = n
    j = m
    while i > 0 and j > 0:
        if line1[i - 1] == line2[j - 1]:


            tot.append(line1[i - 1])

            i -= 1
            j -= 1

        elif qwa[i - 1][j] == qwa[i][j]:
            i -= 1
        else:
            j -= 1
    tot = tot[::-1]
    return tot
line1='abcabaac'
line2='baccbca'
print(maxsequence(line1,line2))


'''Даны две последовательности целых чисел 
Выяснить, является ли вторая последовательность подпоследовательностью первой, то есть можно ли из
 первой вычеркнуть некоторые члены так, чтобы осталась вторая.'''


def subsequence(line1, line2):
    x, i, j = 0, 0, 0

    while i < len(line1):
        if line1[i] == line2[j]:

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


line1 = str(input('Введите первую последовательность: '))
line2 = str(input('Введите вторую последовательность: '))
print(subsequence(line1, line2))
'''На вершине лесенки, содержащей N ступенек, находится мячик, который начинает прыгать по ним вниз, 
к основанию. Сначала мячик может прыгнуть максимум на N/2, но с каждым ударом о ступеньку эта величина
 сокращается вдвое пока он не начинает катиться, перекатываясь с одной ступеньке на другую. 
 Так мячик может прокатиться ещё N/16 ступенек.

Определите число всевозможных "маршрутов" мячика и найдите максимально возможную длину лестницы N.'''

def countr(N, max_jump):
    if N == 1:
        return 1
    routes = 0
    for i in range(1, min(N//2 + 1, max_jump + 1)):
        routes += countr(N - i, i * 2)
    return routes

max_length = 0
max_routes = 0
for N in range(1, 6):
    routes = countr(N, N // 2)
    if routes > max_routes:
        max_routes = routes
        max_length = N

print("Максимально возможная длина :", max_length)
print("Число возможных маршрутов мячика:", max_routes)