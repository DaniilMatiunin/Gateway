
'''С клавиатуры в одной строке вводится произвольное количество вещественных чисел. Запишите их в
 файл, расположив каждое число на отдельной строке. Полученный таким образом файл,
 нужно считать, загрузите список чисел, вычислите их сумму, максимум и минимум, дописать эти значения в конец файла.

Выполните программу несколько раз, убедитесь, что новые значения учитываются при подсчете.

Если файл прочитать не удается, программа должна прекратить чтение и сообщить об этом пользователю'''
numb = input("Введите числа ").split()
with open('Computer Science/example.txt', 'w') as f:
    for x in numb:
        f.write(str(x) +'\n')



try:
    with open('Computer Science/example.txt','r') as f:
        a=[int(x.strip()) for x in f.readlines()]
    summ=sum(a)
    maxi=max(a)
    mini=min(a)

    with open('Computer Science/example.txt','a') as f:
        f.write(f" {summ}\n")
        f.write(f" {maxi}\n")
        f.write(f" {mini}\n")

except Exception as ex :
    print(f"Ошибка  {ex}")


'''Измените предыдущую задачу так, чтобы пользователь мог вводить любые символы, а программа 
записывала бы их в файл. Происходить это должно в цикле несколько раз, и новые данные должны дописываться
 в файл. После чего вне зависимости от ошибок чтения файла, программа должна выполнять 
подсчет суммы, максимума и минимума. И дописать эти значения в конец файла.'''
def writing(file):
    try:
        with open(file, 'a') as f:
            wr = input("Введите что-то")
            while wr.lower() != '':
                f.write(wr + '\n')
                wr = input("Введите что-то")
        print("Успешно.")
    except Exception as e:
        print(f"Ошибка {e}")
def calc(file):
    try:
        with open(file, 'r') as f:
            lines = f.readlines()
        a = []
        for line in lines:
            try:
                a.append(float(line.strip()))
            except ValueError:
                pass

        summ= sum(a)
        maxi = max(a)
        mini = min(a)

        with open(file, 'a') as f:
            f.write(f"Сумма: {summ}\n")
            f.write(f"Максимум: {maxi}\n")
            f.write(f"Минимум: {mini}\n")

        print("succses")

    except Exception as e:
        print(f"Ошибка  {e}")

file = "Computer Science/Example.txt"

writing(file)
calc(file)
'''где строка обозначает ряд, столбец - место (0 - свободно, 1 - занято).

Напишите программу, которая позволит пользователю увидеть количество свободных мест, общее
 число мест в зале, число свободных мест в зале и в каждом ряду, а также, 
введя номер ряда и места, получить информацию - свободно оно или нет.'''
def calcseats(file):
    with open(file, 'r') as f:
        rows = f.readlines()
    list_of_seats = [list(map(int, row.strip().split())) for row in rows]
    return list_of_seats
def calc(list_of_seats):
    free=0

    for x in list_of_seats:

        print(x)
        free+=x.count(0)
    print(f'свободных {free} мест ')
    return free
def all_seats(list_of_seats):
    k=1
    alll=0
    for x in list_of_seats:
        print(f'в{k} ряду {len(x)} мест ')
        alll+=len(x)
        k+=1
    print(f"всего мест {alll}")

def free_in_row(lists):
    k=1
    for x in list:
        print(f'в{k} ряду свободных {x.count(0)} мест ')
        k+=1
def isit(lists,n,r):
    if lists[r - 1][n - 1] == 0:
        print('free')
    else:
        print('booked')



n,r=map(int,input('введите номер места и ряда ').split())
isit(calcseats('Computer Science/Example.txt'),n,r)
calc(calcseats('Computer Science/Example.txt'))
all_seats(calcseats('Computer Science/Example.txt'))
'''Напишите программу, вычисляющую произведение матриц. При этом исходные матрицы и матрица продукт
 находятся в файлах, в программе может храниться только по одному элементу каждой из матриц.

 После проведения расчётов выведите результат в виде:'''
import numpy as np


def matrixing(file1):
    with open(file1,'r') as f1:
        matrixo=f1.readlines()
        matrix = [list(map(int, x.strip().split())) for x  in matrixo]

        return(matrix)
A=np.array(matrixing('Computer Science/Example.txt'))
B=np.array(matrixing('Computer Science/Example1.txt'))

pr=A*B



def printing(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

print("Матрица 1:")
printing(A)
print("\nМатрица 2:")
printing(B)
print("\n умножениe матриц:")
printing(pr)
def printing1(matrix):
    for row in matrix:
        for i in row:
            print(i, end=', ')
printing1(A)
print('X')
printing1(B)
print('=')
printing1(pr)
'''Напишите программу которая ищет по имени на компьютере этот файл с лабораторной работой и выводит полный (абсолютный) путь до него.'''

import os

def findf(file, tpath):
    for dirpath, dirnames, files in os.walk(tpath):
        if file in files:
            return os.path.join(dirpath, file)

    return None


filename = "Laba6.py"
tpath = "C:/"
file_path = findf(filename,tpath)

if file_path:
    print(f"путь файла '{filename}' ")
    print(file_path)
else:
    print(f"файл '{filename}' не найден.")
