#Ques_8
import math
class Shape:
    def __init__(self, colour):
        self.colour = colour

class Circle(Shape):
    def __init__(self, colour, radius):
        super().__init__(colour)
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, colour, length, breadth):
        super().__init__(colour)
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth

class Square(Rectangle):
    def __init__(self, colour, side):
        super().__init__(colour, side, side)

class Triangle(Shape):
    def __init__(self, colour, base, height):
        super().__init__(colour)
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

# Example usage
circle = Circle("Red", 5)
rectangle = Rectangle("Blue", 10, 20)
square = Square("Green", 15)
triangle = Triangle("Yellow", 10, 5)

print(circle.calculate_area())
print(rectangle.calculate_area())
print(square.calculate_area())
print(triangle.calculate_area())