'''В операционной системе MS-DOS первые два байта ЕХЕ-файлов равны 0100110101011010. Это инициалы "MZ"
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


