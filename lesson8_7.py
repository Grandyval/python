# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
# число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив
# сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.
class Complex():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b>0:
            return (f'{self.a}+{self.b}i')
        elif self.b<0:
            return (f'{self.a}{self.b}i')
        else:
            return (f'{self.a}')


    def __add__(self, other):
        return Complex(self.a+other.a, self.b+other.b)

    def __mul__(self, other):
        x1=self.a
        x2=other.a
        y1=self.b
        y2=other.b
        return Complex((x1*x2-y1*y2), (x1*y2+x2*y1))

complex1 = Complex(3,5)
complex2 = Complex(10, -3)

print(complex1 + complex2)
print(complex1 * complex2)