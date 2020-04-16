"""Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу:
длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т"""


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width= width
        self.__weight = 25
        self.__depth = 10

    def mass(self):
        mass_ = (self._length * self._width * self.__weight * self.__depth) / 1000
        print(f'Mass of asphalt required to cover the roadbed in deprh - {self.__depth}, length - {self._length}, '
              f'weight - {self._width} equal {mass_:.2f} tons')


mass_asphalt = Road(7000,30)
mass_asphalt.mass()
