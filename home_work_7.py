import random as rd


# Задание 1
class Matrix:
    def __init__(self, data):
        self._data = data

    def check_matrix(self, matrix2):
        if len(self._data) != len(matrix2._data):
            return False
        else:
            for i in range(len(self._data)):
                if len(self._data[i]) != len(matrix2._data[i]) and len(self._data[0]) != len(self._data[i]):
                    return False
        return True

    def __str__(self):
        s = ""
        for i in self._data:
            for j in i:
                if len(str(j)) > 2:
                    s = s + str(j) + " "
                elif len(str(j)) > 1:
                    s = s + str(j) + "  "
                else:
                    s = s + str(j) + "   "
            s = s + "\n"

        return s

    def __add__(self, other):
        if not self.check_matrix(other):
            return "Error"
        sum_data = []
        for i in range(len(self._data)):
            sum_data1 = []
            for j in range(len(self._data[i])):
                sum_data1.append(self._data[i][j] + other._data[i][j])
            sum_data.append(sum_data1)
        return Matrix(sum_data)


l = [[rd.randint(0, 9) for i in range(10)] for j in range(9)]
matrix1 = Matrix(l)
l = [[rd.randint(0, 9) for i in range(10)] for j in range(9)]
matrix2 = Matrix(l)
sum_matrix = matrix1 + matrix2
print(sum_matrix)


# Задание 2
class Clothes:
    def __init__(self, title):
        self._title = title


class Coat(Clothes):
    def __init__(self, title, V):
        self._title = title
        self.v = V

    def tissue_consumption(self):
        return self.v / 6.5 + 0.5

    @property
    def v(self):
        return self._v

    @v.setter
    def v(self, V):
        if V > 65:
            self._v = 65
        elif V < 30:
            self._v = 30
        else:
            self._v = V


class Costume(Clothes):
    def __init__(self, title, H):
        self._title = title
        self.h = H

    def tissue_consumption(self):
        return 2 * self.h + 0.3

    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, H):
        if H < 0.8:
            self._h = 0.8
        elif H > 2.5:
            self._h = 2.5
        else:
            self._h = H


a = Coat("пальто", 54)
print(a.tissue_consumption())
b = Costume("костюм", 4)
print(b.tissue_consumption())


# Задание 3
class Cell:
    def __init__(self, count):
        self._count = count

    def __add__(self, other):
        return Cell(self._count + other._count)

    def __sub__(self, other):
        if self._count - other._count < 0:
            print("Error")
            return
        else:
            return Cell(self._count - other._count)

    def __mul__(self, other):
        return Cell(self._count * other._count)

    def __truediv__(self, other):
        if other._count == 0:
            print("Ошибка деления на ноль")
            return
        else:
            return Cell(self._count // other._count)

    def make_order(self, n):
        if n <= 0:
            return "Error"
        s = ""
        for i in range(1, self._count):
            s = s + "*"
            if (i % n) == 0:
                s = s + "/" + str(n) + "\n"
        return s


a = Cell(40)
b = Cell(25)
c = a / b
d = a * b
print(c._count, d._count)
print(b.make_order(7))
