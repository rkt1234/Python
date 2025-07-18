# Abstraction hides internal details and shows only the functionality.

# Python provides ABC (Abstract Base Class) using the abc module.

# If you inherit a abstract class then the child class has to implement all the abstract methods of the parent class else the child class
# will also be considered as Abstract class


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

c = Circle(5)
print(c.area())

# ❗ You can't instantiate Shape directly because it has an abstract method.
