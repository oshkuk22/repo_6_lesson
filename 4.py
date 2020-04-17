"""Реализуйте базовый класс Car. У данного класса должны быть следующие
атрибуты: speed, color, name, is_police (булево).  А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько
дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен
показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
 Выполните вызов методов и также покажите результат."""


class Car:
    def __init__(self, speed, color, is_police):
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def show_speed(self):
        print(f'Speed : {self.speed}')

    def go(self):
        print('Car went')

    def stop(self):
        print('Car stop')

    def turn(self, direction):
        print(f'Car turn on {direction}')


class TownCar(Car):
    def show_speed(self):
        if self.speed >= 60:
            print(f'Town car is exceeding the speed limit by : {self.speed - 60}')
        else:
            print(f'Speed : {self.speed}')


class SportCar(Car):
    def info(self):
        print(f'Sport car, color : {self.color}, speed : {self.speed}')


class WorkCar(Car):
    def show_speed(self):
        if self.speed >= 40:
            print(f'Work car is exceeding the speed limit by : {self.speed - 40}')
        else:
            print(f'Speed : {self.speed}')


class PoliceCar(Car):
    def info(self):
        if self.is_police:
            print('Police car')
        else:
            print('Not police car')


car_ = Car(45, 'red', True)
print(car_.speed)
print(car_.color)
print(car_.is_police)
car_.go()
car_.stop()
car_.show_speed()
car_.turn('left')

car_1 = SportCar(45, 'red', True)
car_1.info()

car_2 = WorkCar(45, 'red', True)
car_2.show_speed()

car_2 = TownCar(95, 'white', True)
car_2.show_speed()

car_3 = PoliceCar(45, 'red', True)
car_3.info()
