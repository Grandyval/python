# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в
# качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с
# ошибкой.

class OwnZeroDivizion(Exception):
    pass

a = int(input("Введите делимое: "))
b = int(input("Введите делитель: "))
try:
    if b == 0:
        raise OwnZeroDivizion
    else:
        c = a / b
        print(c)
except OwnZeroDivizion:
    print("На ноль делить нельзя")

