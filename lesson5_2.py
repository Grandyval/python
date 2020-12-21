# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
# подсчет количества строк, количества слов в каждой строке.

with open(file="lesson5_2.txt", encoding="UTF-8", mode="r") as test:
    str_num=0
    for line in test:
        str_num += 1
        print(f"В {str_num} строке {len(line.split())} слов")
    print(f"\nВсего {str_num} строк")

