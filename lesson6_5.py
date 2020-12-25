# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
# метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать
# переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Strationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки {self.title}")

class Pen(Strationery):
    def __init__(self):
        self.title = "ручкой"

class Pencil(Strationery):
    def __init__(self):
        self.title = "карандашом"

class Handle(Strationery):
    def __init__(self):
        self.title = "маркером"



test=Strationery('фломастером')
test.draw()

test=Pen()
test.draw()

test=Pencil()
test.draw()

test=Handle()
test.draw()