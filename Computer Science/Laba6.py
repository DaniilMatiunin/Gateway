
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

''' В операционной системе MS-DOS первые два байта ЕХЕ-файлов равны 0100110101011010. Это инициалы "MZ" 
создателя ЕХЕ-формата Марка Збиковски (Mark Zbikowski). Напишите функцию, проверяющую эти байты у файла,
 заданного ее 
аргументом, и возвращающую 1, если это ЕХЕ-файл, и 0 в противном случае.'''
def exee(file):
    with open(file, 'rb') as f:
        bytese = f.read(2)
        return int(bytese == b'MZ')

file = 'Computer Science/Messe.exe'
print(exee(file))
'''Напишите программу копирующую файл «ИмяФайла» не производя чтения его содержимого (т.е. без привязке к его содержимомому или какой либо иной 
интерпритации хранящийся там информации) в файл «Copy ИмяФайла».'''
import shutil
def copy_file(filename1, filename2):
    shutil.copyfile(filename1, filename2)



with open('Copy ИмяФайла', 'w'):
    pass

filename1 = 'Computer Science/Example.txt'
filename2 = 'Copy ИмяФайла'
copy_file(filename1, filename2)
'''Дан телефонный справочник в формате JSON:

[  {  "имя":"...",  "телефоны":[  {  "описание":"...",  "номер":"..."  },  {  "описание":"...",  "номер":"..."  }  ]  },  ...
Программа должна позволять (предоставлять функции):

загружать информацию из справочника;
выполнять поиск контактов по номеру телефона;
выполнять поиск контактов по имени;
добавлять контакт;
удалять контакты по имени;
удалять номер телефона из контактов;
сохранять справочник в файл.'''
file=input('введите название файла')
def loadbook(file):
    with open(file, 'r') as f:
        contacts = f.readlines()

contacts=loadbook(file)

def search_by_number(contacts,number):
    for contact in contacts:
        for phone in contact["телефоны"]:
            if phone["номер"] == number:
                return contact
    return None

def search_name(contacts, name):
    for contact in contacts:
        if contact["имя"] == name:
            return contact
    return None

def addcontact(contacts,contact):
    contacts.append(contact)
    print('Done')


def removecontactsname(contacts, name):
    newcontacts = [contact for contact in contacts if contact["имя"] != name]
    print('Done')

def remove_number(contacts ,name, number):
    for contact in contacts:
        if contact["имя"] == name:
            contact["телефоны"] = [phone for phone in contact["телефоны"] if phone["номер"] != number]
    print('Done')


def save_phonebook(contacts,filename):
    with open(filename, 'w') as fi:
        fi.write(contacts)
        print('Done')


x=int(input('1введите номер операции:загружать информацию из справочника;'
            '2 выполнять поиск контактов по номеру телефона;'
            '3 выполнять поиск контактов по имени;'
            '4 добавлять контакт;'
            '5 удалять контакты по имени;'
            '6 удалять номер телефона из контактов;'
            '7 сохранять справочник в файл.'))
if x==1:
    print(contacts)
if x==2:
    num=input('введите известную характеристикуЖ')
    print(search_by_number(contacts, num))


if x == 3:
    name=input('введите известную характеристикуЖ')
    print(search_name(contacts, name))
if x == 4:
    contact=input('введите известную характеристикуЖ')
    print(addcontact(contacts, contact))
if x == 5:
    name = input('введите известную характеристикуЖ')
    print(removecontactsname(contacts, name))
if x == 6:
    name = input('введите известную характеристикуЖ')
    num = input('введите известную характеристикуЖ')
    remove_number(contacts ,name, num)
if x ==7 :
    filename = input('введите название файла')
    save_phonebook(contacts, filename)


