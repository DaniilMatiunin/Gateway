
import multiprocessing.dummy as multiprocessing
from os import getpid
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import numpy as np

'''Напишите программу реализующую каскадное скалярное произведение векторов.'''
from concurrent.futures import ThreadPoolExecutor, as_completed
import numpy as np

vex1 = np.array(list(map(float, input('Введите координаты  вектора 1 через пробел: ').split())))
vex2 = np.array(list(map(float, input('Введите координаты  вектора 2 через пробел: ').split())))

sum = 0

# Создание ThreadPoolExecutor с 4 рабочими потоками
with ThreadPoolExecutor(max_workers=4) as pool:
    # Запуск задачи асинхронно
    results = [pool.submit(lambda fx: fx[0] * fx[1], [vex1[i], vex2[i]]) for i in range(len(vex1))] #submit запускает в потоке  функцию
    # Ожидание результата и получение его
    for future in as_completed(results):
        sum += future.result()

print(f'Скалярное произведение векторов  {sum}')
'''vНапишите программу разделяющую матрицы ни подматрицы, осуществляющую паралельное 
перемножение матриц и объединяющую результаты в одну матрицу.'''
def scalarpool(vex):
    sum = 0
    with ThreadPoolExecutor() as executor:
        results = [executor.submit(lambda fx: fx[0] * fx[1], [vex[0][i], vex[1][i]]) for i in range(len(vex[0]))]
        for future in as_completed(results):
            sum += future.result()
    return sum


def Putmatrix():
    return np.array(eval(input('Введите матрицу  ')))


def makevec(matrix, axis=0):
    vectors = []
    if axis != 0:
        matrix = matrix.transpose()
    if len(list(matrix.shape)) <= 1:
        vectors = [list(matrix)]
    else:
        for line in matrix:
            vectors.append(list(line))
    return vectors


def concurrentMatrixProduct(vs1, vs2):
    with ThreadPoolExecutor() as executor:
        holder = [0] * len(vs1) * len(vs2)
        index = 0
        for v1 in vs1:
            for v2 in vs2:
                holder[index] = [v1, v2]
                index += 1
        results = list(executor.map(scalarpool(), holder))
        results = np.array([results]).reshape(len(vs1), len(vs2))
        return results

vectors1 = makevec(Putmatrix())


vectors2 = makevec(Putmatrix(), axis=1)
print()
print(concurrentMatrixProduct(vectors1, vectors2))
'''Проанализируйте возможность распаралеливания этого алгаритма
 и напишите соответствующую программу, оценити сокращение времени работы.'''
def Floid(A, n):
    F = A.copy()
    for k in range(n):
        for i in range(n):
            for j in range(n):
                A[i,j] = min(A[i,j],A[i,k]+A[k,j])
    return F
def Floidst3(A,k):
    for i in range(len(A)):
        for j in range(len(A)):
            A[i, j] = min(A[i, j], A[i, k] + A[k, j])
    return A

pos= [[0, 5, np.inf, 10],
             [np.inf, 0, 3, np.inf],
             [np.inf, np.inf, 0,   1],
             [np.inf, np.inf, np.inf, 0]
             ]
sum =[]
n=4
with ThreadPoolExecutor(max_workers=n) as executor:
    for k in range(len(pos)):
        results = [executor.submit(Floidst3,pos,k)]
    for future in as_completed(results):
        sum.append( future.result())
print(pos)
