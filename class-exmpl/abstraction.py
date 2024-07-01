# Импорт необходимых модулей для создания абстрактного класса и абстрактных методов
from abc import ABC, abstractmethod

# Определение абстрактного класса Shape
class Shape(ABC):
    # Декоратор @abstractmethod указывает, что метод area должен быть переопределен в подклассах
    @abstractmethod
    def area(self):
        pass  # Тело абстрактного метода оставлено пустым

# Определение класса Rectangle, который наследует абстрактный класс Shape
class Rectangle(Shape):
    # Конструктор класса Rectangle принимает два параметра: ширину и высоту прямоугольника
    def __init__(self, width, height):
        self.width = width  # Инициализация атрибута width
        self.height = height  # Инициализация атрибута height

    # Переопределение абстрактного метода area для вычисления площади прямоугольника
    def area(self):
        return self.width * self.height  # Возвращается произведение ширины на высоту

# Создание экземпляра класса Rectangle с шириной 10 и высотой 20
rect = Rectangle(10, 20)

# Вывод площади прямоугольника, используя переопределенный метод area
print(rect.area())  # Выведет 200
