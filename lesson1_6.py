print("Наш спортсмен увеличивает нагрузку на 10% в день")
start = float(input("Веедите пробег первого дня: "))
finish = float(input("Веедите достигаемый результат: "))
days = 1
while start < finish:
    days += 1
    start = start + start * 0.1
print(f"Результат будет достигнут на {days} день")
