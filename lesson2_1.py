# Создать список и заполнить его элементами различных типов данных. Реализовать скрипт
# vпроверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

test_list = [1, 2, 3, "test", True, [4, 6, 6], 88, 0.1]
for el in test_list:
    print(el, type(el))