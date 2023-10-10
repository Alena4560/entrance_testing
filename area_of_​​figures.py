import math
import unittest
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        if self.radius < 0:
            raise ValueError('Радиус не может быть отрицательным')
        return math.pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.is_right_triangle = self.check_if_right_triangle()

    def check_if_right_triangle(self):
        sides = [self.side1, self.side2, self.side3]
        sides.sort()
        return sides[2] ** 2 == sides[0] ** 2 + sides[1] ** 2

    def area(self):
        if any(side <= 0 for side in [self.side1, self.side2, self.side3]):
            raise ValueError('Стороны треугольника должны быть положительными числами')
        s = (self.side1 + self.side2 + self.side3) / 2
        area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        return area


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(3)
        self.assertAlmostEqual(circle.area(), math.pi * 3 ** 2, places=6)

    def test_minus_circle_area(self):
        with self.assertRaises(ValueError) as context:
            circle = Circle(-3)
        self.assertEqual(str(context.exception), 'Радиус не может быть отрицательным')

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0, places=6)

    def test_triangle_right_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle)
        self.assertAlmostEqual(triangle.area(), 6.0, places=6)

    def test_triangle_not_right_triangle(self):
        triangle = Triangle(3, 4, 6)
        self.assertFalse(triangle.is_right_triangle)
        self.assertAlmostEqual(triangle.area(), 5.332682, places=6)

    def test_rectangle_area(self):
        rectangle = Rectangle(4, 5)
        self.assertAlmostEqual(rectangle.area(), 20.0, places=6)


if __name__ == '__main__':
    unittest.main()
