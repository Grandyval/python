number = input("Введите целое положительное число: ")
max_number = int(number[0])
i=0
while i < len(number):
    if max_number < int(number[i]):
        max_number = int(number[i])
    i += 1
print(f"Максимальная цифра в числе: {max_number}")