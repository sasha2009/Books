class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    def __repr__(self):
        return '__repr__ для объекта Car'
    def __str__(self):
        return '__str__ для объекта Car'

my_car = Car('красный', 37281)
print(my_car)
print(str([my_car]))

"""
>>> import datetime
>>> today = datetime.date.today()

Результат метода __str__ объекта даты должен быть прежде всего удо-
бочитаемым. Он призван возвращать легко воспринимаемое человеком
сжатое текстовое представление — то, что вы спокойно можете показать
пользователю. По этой причине, когда мы вызываем функцию str() с объ-
ектом даты, мы получаем нечто похожее на формат даты по ISO:

>>> str(today)
'2017-02-02'

В случае с методом __repr__ идея состоит в том, что его результат должен
быть прежде всего однозначным. Результирующее строковое значение
больше предназначено для разработчиков как средство отладки. И в
связи с этим он должен максимально четко выражать то, чем этот объект
является. Именно поэтому при вызове функции repr() с объектом вы
получите более подробный результат. Он даже будет содержать полное
имя модуля и класса:

>>> repr(today)
'datetime.date(2017, 2, 2)'
"""