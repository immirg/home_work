class Rhombus:
    name = 'Rhombus'

    def __init__(self, side_a: int, angle_a: int = None, angle_b: int = None):
        self.side_a = side_a
        self.angle_a = 180 - angle_b if angle_a is None else angle_a
        self.angle_b = 180 - angle_a if angle_b is None else angle_b

    def __setattr__(self, key, value):
        if key == 'side_a':
            if not isinstance(value, (int, float)) or value <= 0:
                raise ValueError('Не корректно задана сторона А')

        if key == 'angle_a' or key == 'angle_b':
            if not isinstance(value, (int, float)) or not (0 < value < 180):
                raise ValueError('Не корректно задан один из уголов')
            if key == 'angle_a':
                super().__setattr__('angle_b', 180 - value)
            else:
                super().__setattr__('angle_a', 180 - value)

        if key == 'angle_b':
            if 'angle_a' in self.__dict__ and 'angle_b' in self.__dict__ and self.angle_a + value != 180:
                value = 180 - self.angle_a
        super().__setattr__(key, value)

    def __str__(self):
        return f'{self.name}: side_a: {self.side_a}, angle_a: {self.angle_a}, angle_b: {self.angle_b}'


rhombus = Rhombus(side_a=4, angle_b=18)
print(rhombus)
print('*' * 30)
rhombus.angle_a = 33
print(rhombus)
print('*' * 30)
rhombus.angle_b = 111
print(rhombus)

