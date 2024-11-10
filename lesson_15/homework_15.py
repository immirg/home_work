class Rhombus:
    name = 'Rhombus'

    def __init__(self, side_a: int, angle_a: int, angle_b=None):
        self.side_a = side_a
        self.angle_a = angle_a
        self.angle_b = angle_b

    def __setattr__(self, key, value):
        if key == 'side_a':
            try:
                value = float(value)
                if value <= 0:
                    return 'Сторона А должна быть больше 0'
            except ValueError:
                return 'Сторона А не является числом'

        if key == 'angle_a':
            try:
                value = float(value)
                if not (0 < value < 180):
                    return 'Угол А должен быть больше 0 и меньше 180'
            except ValueError:
                return 'Угол А не является числом'

        if key == 'angle_b':
            if 'angle_a' in self.__dict__ and 'angle_b' in self.__dict__ and self.angle_a + value != 180:
                print(f'Значение угла B {value}° некорректно. Угол B установлен как {180 - self.angle_a}°')
            value = 180 - self.angle_a
        super().__setattr__(key, value)

    def __str__(self):
        if 'side_a' in self.__dict__ and 'angle_b' in self.__dict__ and 'angle_b' in self.__dict__:
            return f'{self.name}: side_a: {self.side_a}, angle_a: {self.angle_a}, angle_b: {self.angle_b}'
        else:
            return 'Присутствует ошбика в заданных параметрах'


rhombus = Rhombus(side_a=4, angle_a=24)
print(rhombus)
