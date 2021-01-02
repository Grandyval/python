# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
# также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
# конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
# параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
class Storage():
    def __init__(self, name_storage, quantity):
        self.name_storage = name_storage
        self.quantity = quantity

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


copyer1 = Copyer("Xerox", 1000, "black", 0.5 , "A3")
scanner1 = Scanner("Canon", 200, "black", 0.1 , "led")
printer1 = Printer("HP", 500, "black", 0.1 , 50000)




