ballans_plus = float(input("Введите размер выручки: "))
ballans_minus = float(input("Введите размер издержек: "))
workers = int(input("Сколько в фирме сотрудников: "))
if ballans_plus > ballans_minus:
    print(f"Фирма работает с прибылью. Рентабельность = {int((ballans_plus-ballans_minus)/ballans_plus*100)}%")
    print(f"На каждого сотрудника приходится {(ballans_plus-ballans_minus)/workers:.2f} прибыли")
elif ballans_plus < ballans_minus:
    print("Фирма работает в убыток")
else:
    print("Фирма вышла в ноль")