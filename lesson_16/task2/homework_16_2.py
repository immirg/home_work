class Figure:
    def area_calculation(self):
        pass

    def perimeter_calculation(self):
        pass


class Square(Figure):
    def __init__(self, a):
        self.a = a

    def area_calculation(self):
        area = self.a ** 2
        return area

    def perimeter_calculation(self):
        perimeter = self.a * 4
        return perimeter


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area_calculation(self):
        p = (self.a + self.b + self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def perimeter_calculation(self):
        return self.a + self.b + self.c


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area_calculation(self):
        area = self.a * self.b
        return area

    def perimeter_calculation(self):
        perimeter = 2 * (self.a + self.b)
        return perimeter


if __name__ == '__main__':
    rectangle = Rectangle(5, 10)
    triangle = Triangle(3, 4, 5)
    square = Square(6)

    print(f'Треугольник: площадь - {triangle.area_calculation()}, периметр {triangle.perimeter_calculation()}')
    print(f'Квадрат: площадь - {triangle.area_calculation()}, периметр {triangle.perimeter_calculation()}')
    print(f'Прямоугольник: площадь - {triangle.area_calculation()}, периметр {triangle.perimeter_calculation()}')
