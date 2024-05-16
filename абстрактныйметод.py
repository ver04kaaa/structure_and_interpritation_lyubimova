from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

rectangle = Rectangle(5, 10)
print("Area of rectangle:", rectangle.calculate_area())

circle = Circle(5)
print("Area of circle:", circle.calculate_area())

#Классы Rectangle и Circle наследуются от абстрактного класса Shape
#и должны реализовать метод calculate_area. Таким образом, абстрактные 
#классы позволяют определить общий интерфейс для классов-наследников, но 
#не содержат конкретной реализации