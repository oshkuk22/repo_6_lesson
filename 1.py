"""1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора
в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить
соответствующее сообщение и завершать скрипт."""

import time


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        if self.__color == 'red':
            print('Red')
            time.sleep(7)
            self.__switch_light()
        elif self.__color == 'yellow':
            print('Yellow')
            time.sleep(2)
            self.__switch_light()
        elif self.__color == 'green':
            print('Green')
            time.sleep(6)
            self.__switch_light()
        else:
            print(f' Traffic lights don_t have {self.__color} mode')

    def __switch_light(self):
        if self.__color == 'red':
            self.__color = 'yellow'
            self.running()
        elif self.__color == 'yellow':
            self.__color = 'green'
            self.running()
        else:
            self.__color = "red"
            self.running()


traffic_light = TrafficLight('red')
traffic_light.running()

