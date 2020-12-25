# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.id_polise = is_police

    def info(self):
        return (f"Автомобиль {self.name}, цвет - {self.color}, движется со скоростью {self.speed} км/ч")

    def go(self):
        return "Автомобиль движется"

    def stop(self):
        return "Автомобиль остановился"

    def turn(self, direction):
        return (f"Автомобиль повернул {direction}")


    def show_speed(self):
        return (f"Скорость равна {self.speed} км/ч")

class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return (f"Скорость превышена на {self.speed - 60} км/ч")
        else:
            return (f"Скорость равна {self.speed} км/ч")

class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed>40:
            return (f"Скорость превышена на {self.speed-40} км/ч")
        else:
            return (f"Скорость равна {self.speed} км/ч")

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


test = Car(10, 'красный', 'Toyota', True)
print(test.info())

test = TownCar(80, 'красный', 'Toyota')
print(test.info())
print(test.show_speed())

test = SportCar(200, 'красный', 'Toyota')
print(test.info())
print(test.turn('влево'))