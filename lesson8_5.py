# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём
# оргтехники на склад и передачу в определенное подразделение компании. Для хранения
# данных о наименовании и количестве единиц оргтехники, а также других данных, можно
# использовать любую подходящую структуру, например словарь.
class Storage():
    def __init__(self, name_storage, quantity):
        self.name_storage = name_storage
        self.quantity = quantity

    def send_tech(self, number): #отправка(количество)
        self.quantity -= number
        return self

    def recieve_tech(self, number): #приемка (количество)
        self.quantity += number
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

storage_copyer1 = Storage(copyer1.name, 10) #начальное состояние склада
storage_printer1 = Storage(printer1.name, 20)
storage_scanner1 = Storage(scanner1.name, 50)

storage_copyer1 = storage_copyer1.recieve_tech(5) #приемка 5 единиц
print(storage_copyer1.name_storage, storage_copyer1.quantity)
storage_scanner1 = storage_scanner1.send_tech(20) #отправка 20 единиц
print(storage_scanner1.name_storage, storage_scanner1.quantity)


