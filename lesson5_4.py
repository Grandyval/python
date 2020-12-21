# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно
# данные. При этом английские числительные должны заменяться на русские. Новый блок строк
# должен записываться в новый текстовый файл.

trans = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

test_en = open(file="lesson5_4_en.txt", encoding="UTF-8", mode="r")
test_ru = open(file="lesson5_4_ru.txt", encoding="UTF-8", mode="w")
for line in test_en:
    test_ru.write(f"{trans.get(line.split()[0])} - {line.split()[2]}\n")
test_en.close()
test_ru.close()