'''Создайте класс "Геометрические фигуры" атрибутами котрого будут: параметры периметр, площадь и координаты некотрой характерной точки или точек (например, центра или вершин). Создайте три класса потомка: треугольник, прямоугольник, круг. Для классов потомков определить функцию инициализации __init__ и функции для вычисления периметра и площади,
 функцию paint выводящую рисунок соответствующей геометрической фигуры с помощью библиотеки matplotlib.'''
import matplotlib.pyplot as plt
import numpy as np


class GeometricFigure:
    def __init__(self, coordinate):
        self.coordinate = coordinate

    def perimeter(self):
        pass

    def area(self):
        pass

    def paint(self):
        pass


class Triangle(GeometricFigure):
    def __init__(self, coordinate):
        super().__init__(coordinate)

    def perimeter(self):
        side1 = np.linalg.norm(self.coordinate[1] - self.coordinate[0])
        side2 = np.linalg.norm(self.coordinate[2] - self.coordinate[1])
        side3 = np.linalg.norm(self.coordinate[0] - self.coordinate[2])
        return side1 + side2 + side3

    def area(self):
        a = np.linalg.norm(self.coordinate[1] - self.coordinate[0])
        b = np.linalg.norm(self.coordinate[2] - self.coordinate[1])
        c = np.linalg.norm(self.coordinate[0] - self.coordinate[2])
        s = (a + b + c) / 2
        return np.sqrt(s * (s - a) * (s - b) * (s - c))

    def paint(self):
        plt.plot([self.coordinate[0][0], self.coordinate[1][0], self.coordinate[2][0], self.coordinate[0][0]],
                 [self.coordinate[0][1], self.coordinate[1][1], self.coordinate[2][1], self.coordinate[0][1]])
        plt.title('Треугольник')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()


class Rectangle(GeometricFigure):
    def __init__(self, coordinate):
        super().__init__(coordinate)

    def perimeter(self):
        side1 = np.linalg.norm(self.coordinate[1] - self.coordinate[0])
        side2 = np.linalg.norm(self.coordinate[2] - self.coordinate[1])
        return 2 * (side1 + side2)

    def area(self):
        side1 = np.linalg.norm(self.coordinate[1] - self.coordinate[0])
        side2 = np.linalg.norm(self.coordinate[2] - self.coordinate[1])
        return side1 * side2

    def paint(self):
        x = [self.coordinate[0][0], self.coordinate[1][0], self.coordinate[2][0], self.coordinate[3][0],
             self.coordinate[0][0]]
        y = [self.coordinate[0][1], self.coordinate[1][1], self.coordinate[2][1], self.coordinate[3][1],
             self.coordinate[0][1]]
        plt.plot(x, y)
        plt.title('Прямоугольник')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()


class Circle(GeometricFigure):
    def __init__(self, coordinate, radius):
        super().__init__(coordinate)
        self.radius = radius

    def perimeter(self):
        return 2 * np.pi * self.radius

    def area(self):
        return np.pi * self.radius ** 2

    def paint(self):
        circle = plt.Circle((self.coordinate[0], self.coordinate[1]), self.radius, fill=False)
        fig, ax = plt.subplots()
        ax.add_artist(circle)
        ax.set_xlim(self.coordinate[0] - self.radius, self.coordinate[0] + self.radius)
        ax.set_ylim(self.coordinate[1] - self.radius, self.coordinate[1] + self.radius)
        plt.title('Круг')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()


triangle = Triangle(np.array([[1, 1], [2, 3.5], [6, 3]]))
print("Периметр треугольника:", triangle.perimeter())
print("Площадь треугольника:", triangle.area())
triangle.paint()

rectangle = Rectangle(np.array([[3, 3], [6, 0], [6 , 6], [0, 6]]))
print("Периметр прямоугольника:", rectangle.perimeter())
print("Площадь прямоугольника:", rectangle.area())
rectangle.paint()

circle = Circle(np.array([4, 5]), 9)
print("Периметр круга:", circle.perimeter())
print("Площадь круга:", circle.area())
circle.paint()
'''Конструктор от списка списков. Гарантируется, что списки состоят из чисел, не пусты и все имеют одинаковый размер. Конструктор должен копировать содержимое списка списков, т.е. при изменении списков, от которых была сконструирована матрица, содержимое матрицы изменяться не должно.
Метод __str__, переводящий матрицу в строку. При этом элементы внутри одной строки должны быть разделены знаками табуляции, а строки — переносами строк. После каждой строки не должно быть символа табуляции и в конце не должно быть переноса строки.
Метод size без аргументов, возвращающий кортеж вида (число строк, число столбцов).
__add__, принимающий вторую матрицу того же размера и возвращающий сумму матриц. В случае, если две матрицы сложить невозможно, должно выводиться сообщение об ошибке.
__mul__, таким образом, чтобы матрицы можно было умножать на скаляры и на другие матрицы. В случае, если две матрицы перемножить невозможно, должно выводиться сообщение об ошибке.
__rmul__, делающий то же самое, что и __mul__. Этот метод будет вызван в том случае, аргумент находится справа.
 Для реализации этого метода в коде класса достаточно написать __rmul__ = __mul__.
Реализуйте статический метод transposed, принимающий Matrix и возвращающий транспонированную матрицу.'''


class Matrix:
    def __init__(self, matrix):
        self.matrix = [row[:] for row in matrix]

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])

    def size(self):
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        return rows, cols

    def __add__(self, other):
        if self.size() != other.size():
            print("Матрицы должны иметь одинаковый размер для сложения.")
            return None
        result = []
        for i in range(len(self.matrix)):
            row = []

            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(row)
        return Matrix(result)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = []
            for i in range(len(self.matrix)):
                row = []
                for j in range(len(self.matrix[0])):
                    row.append(self.matrix[i][j] * other)
                result.append(row)
            return Matrix(result)
        elif isinstance(other, Matrix):
            if self.size()[1] != other.size()[0]:
                print("Количество столбцов в 1 матрице должно быть равно количеству строк во 2 матрице для умножения.")
                return None
            result = []
            for i in range(len(self.matrix)):
                row = []
                for j in range(len(other.matrix[0])):
                    total = 0
                    for k in range(len(other.matrix)):
                        total += self.matrix[i][k] * other.matrix[k][j]
                    row.append(total)
                result.append(row)
            return Matrix(result)
        else:
            print("Не тот аргумент для умножения.")
            return None

    __rmul__ = __mul__

    @staticmethod
    def transposed(matrix):
        transposed_matrix = [[matrix.matrix[j][i] for j in range(len(matrix.matrix))] for i in
                             range(len(matrix.matrix[0]))]
        return Matrix(transposed_matrix)


matrix1 = Matrix([[1, 2, 3], [4, 5, 6]])
matrix2 = Matrix([[7, 8, 9], [10, 11, 12]])
print("Матрица 1:")
print(matrix1, '\n')
print("Матрица 2:")
print(matrix2, '\n')

print("Матрица 1 + Матрица 2:")
print(matrix1 + matrix2, '\n')

print("Матрица 1 * 2:")
print(matrix1 * 2, '\n')

print("Матрица 1 * Матрица 2:")
print(matrix1 * matrix2, '\n')

print("Транспонированная матрица 1:")
print(Matrix.transposed(matrix1))
'''Создайте класс Vector наследующий все атрибуты класса Matrix, методы реализованные в классе из задания
 3 предыдущей
 лабораторной и обладающим методом векторного произведения векторов.'''


class Vector(Matrix):
    def __init__(self, vector):
        super().__init__([[elem] for elem in vector])

    def vector_product(self, other):
        if self.size() != (3, 1) or other.size() != (3, 1):
            print("Перекрестное произведение определено только для трехмерных векторов.")
            return None
        x1, y1, z1 = self.matrix[0][0], self.matrix[1][0], self.matrix[2][0]
        x2, y2, z2 = other.matrix[0][0], other.matrix[1][0], other.matrix[2][0]
        result_x = y1 * z2 - z1 * y2
        result_y = z1 * x2 - x1 * z2
        result_z = x1 * y2 - y1 * x2
        return Vector([result_x, result_y, result_z])


vector1 = Vector([1, 2, 3])
vector2 = Vector([4, 5, 6])
print("Вектор 1:")
print(vector1, '\n')
print("Вектор 2:")
print(vector2, '\n')

print("Вектор 1 + Вектор 2:")
print(vector1 + vector2, '\n')

print("Вектор 1 * 2:")
print(vector1 * 2, '\n')
'''Измените классы из 1 задания следующим образом.

Создайте класс "Параметры" состаящий из двух атрибутов: значения и описания этого параметра (т.е. строки).
 Сделайте каждый
 параметр созданных в задании 1 классов объектом класса "Параметры".

Создайте библиотеку функций для вычисления площадей и периметров двумя способами:

соберите функции в класс и объявите их как статические (для вычисления параметров фигур вызывайте функции 
из этого класса);

соберите функции в класс с помощью композиции (т.е. создавая внутри этого класса объекты соответствующих 
геометрических фигур и проводя соответствующие вычисления)'''
class parameters:

    def __init__(self, value, description):
        self.value = value
        self.description = description

    class calculations:

        @staticmethod
        def area_triangle(a, b, c):

            S = 0.5 * (a[0] - c[0]) * (b[1] - c[1]) - (b[0] - c[0]) * (a[1] - c[1])
            return abs(S)

        @staticmethod
        def perimeter_triangle(a, b, c):
            AB = (b[0] - a[0], b[1] - a[1])
            BC = (c[0] - b[0], c[1] - b[1])
            AC = (c[0] - a[0], c[1] - a[1])
            AB = (AB[0] ** 2 + AB[1] ** 2) ** 0.5
            BC = (BC[0] ** 2 + BC[1] ** 2) ** 0.5
            AC = (AC[0] ** 2 + AC[1] ** 2) ** 0.5
            return AB + BC + AC

        @staticmethod
        def area_rectangle(a, b, c, d):
            S = 0.5 * abs((a[0] * b[1]) + (b[0] * c[1]) + (c[0] * d[1]) + (d[0] * a[1]) -
                          (b[0] * a[1]) - (c[0] * b[1]) - (d[0] * c[1]) - (a[0] * d[1]))
            return S

        @staticmethod
        def perimeter_rectangle(a, b, c, d):
            AB = (b[0] - a[0], b[1] - a[1])
            BC = (c[0] - b[0], c[1] - b[1])
            CD = (d[0] - c[0], d[1] - c[1])
            AD = (d[0] - a[0], d[1] - a[1])
            AB = (AB[0] ** 2 + AB[1] ** 2) ** 0.5
            BC = (BC[0] ** 2 + BC[1] ** 2) ** 0.5
            CD = (CD[0] ** 2 + CD[1] ** 2) ** 0.5
            AD = (AD[0] ** 2 + AD[1] ** 2) ** 0.5
            return AB + BC + CD + AD

        @staticmethod
        def area_circle(r):
            S = 3.14 * r ** 2
            return S

        @staticmethod
        def perimeter_circle(r):
            return 2 * 3.14 * r

'''соберите функции в класс с помощью композиции (т.е. создавая внутри этого класса объекты
 соответствующих геометрических фигур и проводя соответствующие вычисления).'''
class CalculationOFParameters:

    def area_triangle(a, b, c):
        figure = triangle(a, b, c)
        figure.area()

    def perimeter_triangle(a, b, c):
        figure = triangle(a, b, c)
        figure.perimeter()

    def area_rectangle(a, b, c, d):
        figure = rectangle(a, b, c, d)
        figure.area()

    def perimeter_rectangle(a, b, c, d):
        figure = rectangle(a, b, c, d)
        figure.perimeter()

    def area_circle(r, coord):
        figure = rectangle(r, coord)
        figure.area()

    def perimeter_circle(r, coord):
        figure = rectangle(r, coord)
        figure.perimeter()


class GeometricShapes:

    def __init__(self, area, perimeter, coordinates):
        self.area = parameters(*area)
        self.perimeter = parameters(*perimeter)
        self.coordinates = parameters(*coordinates)


class triangle(GeometricShapes):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        GeometricShapes.__init__(self, self.area(), self.perimeter(), self.__dict__)

    def area(self):

        S = 0.5 * (self.a[0] - self.c[0]) * (self.b[1] - self.c[1]) - (self.b[0] - self.c[0]) * (self.a[1] - self.c[1])
        return abs(S)

    def perimeter(self):
        AB = (self.b[0] - self.a[0], self.b[1] - self.a[1])
        BC = (self.c[0] - self.b[0], self.c[1] - self.b[1])
        AC = (self.c[0] - self.a[0], self.c[1] - self.a[1])
        AB = (AB[0] ** 2 + AB[1] ** 2) ** 0.5
        BC = (BC[0] ** 2 + BC[1] ** 2) ** 0.5
        AC = (AC[0] ** 2 + AC[1] ** 2) ** 0.5
        return AB + BC + AC

    def paint(self):
        x = [self.a[0], self.b[0], self.c[0], self.a[0]]
        y = [self.a[1], self.b[1], self.c[1], self.a[1]]
        plt.plot(x, y)
        plt.show()


class rectangle(GeometricShapes):

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        GeometricShapes.__init__(self, self.area(), self.perimeter(), self.__dict__)

    def area(self):
        S = 0.5 * abs(
            (self.a[0] * self.b[1]) + (self.b[0] * self.c[1]) + (self.c[0] * self.d[1]) + (self.d[0] * self.a[1]) -
            (self.b[0] * self.a[1]) - (self.c[0] * self.b[1]) - (self.d[0] * self.c[1]) - (self.a[0] * self.d[1]))
        return S

    def perimeter(self):
        AB = (self.b[0] - self.a[0], self.b[1] - self.a[1])
        BC = (self.c[0] - self.b[0], self.c[1] - self.b[1])
        CD = (self.d[0] - self.c[0], self.d[1] - self.c[1])
        AD = (self.d[0] - self.a[0], self.d[1] - self.a[1])
        AB = (AB[0] ** 2 + AB[1] ** 2) ** 0.5
        BC = (BC[0] ** 2 + BC[1] ** 2) ** 0.5
        CD = (CD[0] ** 2 + CD[1] ** 2) ** 0.5
        AD = (AD[0] ** 2 + AD[1] ** 2) ** 0.5
        return AB + BC + CD + AD

    def paint(self):
        x = [self.a[0], self.b[0], self.c[0], self.d[0], self.a[0]]
        y = [self.a[1], self.b[1], self.c[1], self.d[1], self.a[1]]
        plt.plot(x, y)
        plt.show()


class circle1(GeometricShapes):

    def __init__(self, r, coord):
        self.r = r
        GeometricShapes.__init__(self, self.area(), self.perimeter(), coord)

    def area(self):
        S = 3.14 * self.r ** 2
        return S

    def perimeter(self):
        return 2 * 3.14 * self.r

    def paint(self):
        draw_circle = plt.Circle(self.coordinates, self.r, fill=False)
        plt.xlim(xmin=-15, xmax=15)
        plt.ylim(ymin=-15, ymax=15)
        plt.gcf().gca().add_artist(draw_circle)
        plt.show()