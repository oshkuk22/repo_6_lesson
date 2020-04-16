"""Реализовать базовый класс Worker (работник), в котором определить
атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени
сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров)."""


class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            'Chief': {'wage': 60000, 'bonus': 25000},
            'Deputy chief': {'wage': 50000, 'bonus': 21000},
            'employee': {'wage': 35000, 'bonus': 13000}
        }


class Position(Worker):
    def get_full_name(self):
        print(f'Name : {self.name}\nSurname : {self.surname}')

    def get_total_income(self):
        income_ = self._income[self.position]['wage'] + self._income[self.position]['bonus']
        print(f'Name Surname : {self.name} {self.surname}\nPosition : {self.position}\nTotal income : {income_}')


worker = Position('Ivan', 'Ivanov', 'Deputy chief')
worker.get_full_name()
worker.get_total_income()





