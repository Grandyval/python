# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных на
# склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
# максимум возможностей, изученных на уроках по ООП.
class MyExeption(Exception):
    pass

class Storage():
    def __init__(self, name_storage, quantity):
        self.name_storage = name_storage
        self.quantity = quantity



    def send_tech(self, number): #отправка(количество)
        try:
            if type(number) == int:
                self.quantity -= number
            else:
                raise MyExeption
        except MyExeption:
            print('Количество - не число')
        return self

    def recieve_tech(self, number): #приемка (количество)
        try:
            if type(number) == int:
                self.quantity += number
            else:
                raise MyExeption
        except MyExeption:
            print('Количество - не число')
        return self


class Technic():
    def __init__(self, name,  price, color, volume, type_technic):
        self.name = name
        self.type_technic = type_technic
        self.price = price
        self.color = color
        self.volume = volume


class Printer(Technic):
    def __init__(self, name, price, color, volume, resurse):
        super().__init__(name, price, color, volume, type_technic = 'Принтер')
        self.resurse = resurse

class Scanner(Technic):
    def __init__(self, name, price, color, volume, type_lamp):
        super().__init__(name, price, color, volume, type_technic = 'Сканер')
        self.type_lamp = type_lamp

class Copyer(Technic):
    def __init__(self, name, price, color, volume, format_paper):
        super().__init__(name, price, color, volume, type_technic="Копир")
        self.format_paper = format_paper


copyer1 = Copyer("Xerox 3220", 1000, "black", 0.5 , "A3")
scanner1 = Scanner("Canon 200", 200, "black", 0.1 , "led")
printer1 = Printer("HP 1200", 500, "black", 0.1 , 50000)

storage_copyer = Storage(copyer1.name, 10)
storage_printer = Storage(printer1.name, 20)
storage_scanner = Storage(scanner1.name, 50)

storage_copyer = storage_copyer.recieve_tech(5)
print(storage_copyer.name_storage, storage_copyer.quantity)
storage_scanner = storage_scanner.send_tech('20')
print(storage_scanner.name_storage, storage_scanner.quantity)