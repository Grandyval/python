seconds = int(input("Введите, пожалуйста, какое-то количество секунд для преобразования: "))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = seconds - hours * 3600 - minutes * 60
print(f"{hours:02}:{minutes:02}:{seconds:02}")