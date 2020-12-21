# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить
# ее на экран.

with open(file="lesson5_5.txt", encoding="UTF-8", mode="w") as test:
    test.write(input("Введите набор чисел, разделенных пробелами: "))
    test.close()

with open(file="lesson5_5.txt", encoding="UTF-8", mode="r") as test:
    summa  = 0
    for el in test.read().split():
        summa += float(el)
    print(f"Сумма равна {summa}")
