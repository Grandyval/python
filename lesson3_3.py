# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и
# возвращает сумму наибольших двух аргументов.

def my_func(a1, a2, a3):
    list_a=[a1,a2,a3]
    min_a=a1
    for el in list_a: #поиск минимального агрумента
        if el < min_a:
            min_a = el
    list_a.remove(min_a)
    return list_a[0]+list_a[1]

print(my_func(6,-4,41))
