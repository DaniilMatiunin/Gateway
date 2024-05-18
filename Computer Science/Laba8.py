'''Создать класс с двумя переменными. Добавить функцию вывода на экран и функцию изменения этих переменных. Добавить функцию, которая находит сумму значений этих
переменных, и функцию которая находит наибольшее значение из этих двух переменных.'''
import random
class xy:
    def __init__(self,x, y):
        self.x = x
        self.y = y

    def print_(self):
        print(self.x)
        print(self.y)

    def changing(self):
        self.x+=random.randint(1,27)
        self.y-=random.randint(1,5)
        print(self.x)
        print(self.y)

    def summ(self):
        print(self.x + self.y)

    def maxim(self):
        print(max(self.x,self.y))
Work= xy(8,6)
Work.print_()
Work.changing()
Work.summ()
Work.maxim()
'''Составить описание класса многочленов от одной переменной, задаваемых степенью многочлена
и массивом коэффициентов.
 Предусмотреть методы для вычисления значения многочлена для заданного аргумента, операции сложения, вычитания и
 умножения многочленов с получением
нового объекта-многочлена, вывод на экран описания многочлена.'''
class polynomial():
    def __init__(self, degree, components):
        self.degree = degree
        self.components = components

    def evaluate(self, x):
        result = 0
        for i in range(self.degree + 1):
            result += self.components[i] * (x ** i)
        return result
    def adding(self, degree1, components1):
        maxdegree = max(self.degree, degree1)
        allcomponents = [0] * (maxdegree+1)
        for i in range(self.degree+1):
            allcomponents[i] += self.components[i]
        for i in range(degree1+1):
            allcomponents[i] += components1[i]
        return polynomial(maxdegree, allcomponents)

    def substraction(self, degree1, components1):
        maxdegree = max(self.degree, degree1)
        allcomponents = [0] * (maxdegree + 1)
        for i in range(self.degree + 1):
            allcomponents[i] += self.components[i]
        for i in range(degree1 + 1):
            allcomponents[i] -= components1[i]
        return polynomial(maxdegree, allcomponents)
    def multiply(self,degree1,components1):
        totaldeg=self.degree+degree1
        newcomponents=[0]*(totaldeg+1)
        for i in range(self.degree+1):
            for j in range(degree1+1 ):
                newcomponents[i+j]+=self.components[i]*components1[j]
        return polynomial(totaldeg,newcomponents)
    def display(self):
        print("Степень многочлена:", self.degree)
        print("Коэффициенты:", self.components)




polyn = polynomial(3, [3, 4, 5,4])
Addi=polyn.adding(4,[1,1,1,1,4])
Subs=polyn.substraction(4,[1,1,1,1,4])
Mult=polyn.multiply(4,[1,1,1,1,4])
Addi.display()
Subs.display()
Mult.display()
x =int(input('введите значение '))
print(f"Значение многочлена  при x={x}:", polyn.evaluate(x))

'''Составить описание класса для вектора, заданного координатами его концов в трехмерном пространстве. 
Обеспечить операции сложения и вычитания векторов с получением нового вектора (суммы или разности), 
вычисления скалярного произведения 
двух векторов, длины вектора, косинуса угла между векторами.'''
class Vertex():
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def adding(self,x,y,z):
        x1=self.x+x
        y1 = self.y + y
        z1 = self.z + z
        return Vertex(x1,y1,z1)
    def substraction(self,x,y,z):
        x1 = self.x + x
        y1 = self.y + y
        z1 = self.z + z
        return Vertex(x1, y1, z1)
    def scalarproduct(self,x,y,z):
        x1 = self.x * x
        y1 = self.y * y
        z1 = self.z * z
        return Vertex(x1,y1,z1)
    def Vexvolume(self):
        volme=(self.x**2+self.y**2+self.z**2)**(0.5)
    def cos(self,x,y,z):
        volme = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** (0.5)
        volme1 = (x ** 2 + y ** 2 + z ** 2) ** (0.5)
        x1 = self.x * x
        y1 = self.y * y
        z1 = self.z * z
        cos=(x1+y1+z1)/(volme*volme1)
    def display(self):
        print(f'координаты вектора:x {self.x}, y {self.y}, z { self.z}')


vex=Vertex(2,4,5)
addi=vex.adding(3,4,5)
subb=vex.substraction(1,1,1)
scar=vex.scalarproduct(3,4,5)
print('Cумма')
addi.display()
print('Вычитание')
subb.display()
print('произведение')
scar.display()
print(vex.Vexvolume())
print(vex.cos(3,4,5))
'''Создайте структуру с именем train, содержащую поля: название пунктов отправления и назначения,
 время отправления и прибытия. Перегрузить операцию сложения - два поезда можно сложить, 
 если пунк назначения первого совпадает с 
пунктом отправления второго и время прибытия первого раньше чем отправление второго.'''
class startrain:
    def __init__(self, departure, destination, departureTime, arrival):
        self.departure = departure
        self.destination = destination
        self.departureTime = departureTime
        self.arrival = arrival

    def __add__(self, another):
        if self.destination == another.departure and self.arrival < another.departureTime:
            new_train = startrain(self.departure, another.destination, self.departureTime, another.arrival)
            return new_train
        else:
            print("Поезда не могут быть сложены")
            return None



train1 = startrain("Коломнв", "Мурманск", "10:00", "17:00")
train2 = startrain("Мурманск", "Москва", "16:36", "04:00")


new_train = train1 + train2

if new_train:
    print(
        f"Новый поезд из г.{new_train.departure} в г.{new_train.destination} отправляется в {new_train.departure_time} , прибывает в {new_train.arrival_time}")




