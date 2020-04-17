"""Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
метод для каждого экземпляра."""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Start rendering {self.title}')


class Pen(Stationery):
    def draw(self):
        if self.title == 'pen':
            print(f'Start rendering a Pen')


class Pencil(Stationery):
    def draw(self):
        if self.title == 'pencil':
            print(f'Start rendering a Pencil')


class Handle(Stationery):
    def draw(self):
        if self.title == 'handle':
            print(f'Start rendering a Handel')


draw_image = Stationery('pen')
draw_image.draw()

draw_image = Pen('pen')
draw_image.draw()

draw_image = Pencil('pencil')
draw_image.draw()

draw_image = Handle('handle')
draw_image.draw()