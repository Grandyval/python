test_var = 1000

# динамическая типизация
print("Примеры изменения типов переменной")
print(test_var, type(test_var))
test_var = float(test_var)
print(test_var, type(test_var))
test_var = str(test_var)
print(test_var, type(test_var))
age = int(input("Введите срой возраст: "))
name = input("имя: ")
family = input("и фамилию: ")
print(f"Вас зовут: {family} {name}, и ваш возраст: {age}")