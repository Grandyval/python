# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
# декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к
# типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
# реальных данных.

class UserDate():
    def __init__(self, text_date):
        self.text_date = text_date

    @classmethod #если чесно, не понял смысла данной операцииб фактически только синтаксис реализовал
    def number_date(cls,text):
        number = text.split(sep="-")
        return number

    @staticmethod
    def valid(text_date):
        valid_day = {"1": 31, "2": 28, "3": 31, "4": 30, "5": 31, "6": 30, "7": 31, "8": 31, "9": 30, "10": 31,
                     "11": 30, "12": 31}
        day = int(text_date.split(sep="-")[0])
        month = text_date.split(sep="-")[1]
        if (month not in valid_day) or (day>valid_day[month]) :
            return "Некорректная дата"
        else:
            return "Дата корректна"

a = UserDate.number_date("1-1-1")
print(a)

print(UserDate.valid("28-2-1990"))
print(UserDate.valid("29-2-1990"))

