# 1. Инкапсуляция
#
# class Person:
#     def __init__(self):
#         self._age = 0
#
#     def set_age(self, age):
#         if age < 0:
#             return "Возраст не может быть отрицательным"
#         self._age = age
#
#     def get_age(self):
#         return self._age
#
#
# p = Person()
# # p.set_age(25)
# # print(p.get_age())  # Вывод: 25
# print(p.set_age(-5))

#  2. Наследование

# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         return "I am an animal"
#
#
# class Dog(Animal):
#     def speak(self):
#         return "Woof"
#
#
# class Cat(Animal):
#     def speak(self):
#         return "Meow"
#
#
# dog = Dog("Buddy")
# cat = Cat("Kitty")
#
# print(dog.name, dog.speak())  # Вывод: Buddy Woof
#
# print(cat.name, cat.speak())  # Вывод: Kitty Meow

# 3. Полиморфизм

# class Vehicle:
#     def move(self):
#         return "Vehicle is moving"
#
#
# class Car(Vehicle):
#     def move(self):
#         return "Car is driving"
#
#
# class Bicycle(Vehicle):
#     def move(self):
#         return "Bicycle is pedaling"
#
#
# def move(vehicle):
#     return vehicle.move()
#
#
# car = Car()
# bike = Bicycle()
#
# print(move(car))  # Вывод: Car is driving
# print(move(bike))  # Вывод: Bicycle is pedaling

# 4. Абстракция

# from abc import ABC, abstractmethod
# import math
#
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi * self.radius ** 2
#
#
# rect = Rectangle(10, 5)
# circle = Circle(7)
#
# print(rect.area())  # Вывод: 50
# print(circle.area())  # Вывод: ~153.94
