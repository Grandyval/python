# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.

class Matrix():
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list


    def __str__(self):
        temp_str = ''
        for el in self.matrix_list:
            for el1 in el:
                temp_str += (str(el1) + " ")
            temp_str += "\n"
        return temp_str

    def __add__(self, other):
        new_matrix=[]
        for ind,el in enumerate(self.matrix_list):
            new_matrix.append([])
            for ind1, el1 in enumerate(el):
                new_matrix[ind].insert(ind1, self.matrix_list[ind][ind1]+other.matrix_list[ind][ind1])
        return Matrix(new_matrix)


matrix1 = Matrix([[1, 1, 1],[2, 2, 2],[3, 3, 3]])
matrix2 = Matrix([[4, 4, 4],[5, 5, 5],[6, 6, 6]])
print(matrix1)
print(matrix2)
print(matrix1 + matrix2)
