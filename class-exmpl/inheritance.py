# Определение базового класса Vehicle
class Vehicle:
    # Конструктор класса Vehicle, принимающий имя и скорость транспортного средства
    def __init__(self, name, speed):
        self.name = name  # Инициализация атрибута name
        self.speed = speed  # Инициализация атрибута speed

    # Метод для получения скорости транспортного средства
    def get_speed(self):
        return self.speed  # Возвращает скорость транспортного средства

# Определение класса Car, который наследует класс Vehicle
class Car(Vehicle):
    # Конструктор класса Car, принимающий имя, скорость и пробег автомобиля
    def __init__(self, name, speed, mileage):
        super().__init__(name, speed)  # Вызов конструктора базового класса Vehicle для инициализации name и speed
        self.mileage = mileage  # Инициализация атрибута mileage, уникального для класса Car

    # Метод для получения пробега автомобиля
    def get_mileage(self):
        return self.mileage  # Возвращает пробег автомобиля

# Создание экземпляра класса Car с именем "Toyota", скоростью 150 и пробегом 20000
car = Car("Toyota", 150, 20000)

# Вывод скорости и пробега автомобиля, используя методы get_speed и get_mileage
print(car.get_speed(), car.get_mileage())
