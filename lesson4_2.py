# Представлен список чисел. Необходимо вывести элементы исходного списка, значения
# которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для
# формирования списка использовать генератор.
# Пример исходного списка:
# [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат:
# [12, 44, 4, 10, 78, 123].

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_list1 = [el for i,el in enumerate(my_list) if (my_list[i]>my_list[i-1]) and i!=0]
print(my_list1)

