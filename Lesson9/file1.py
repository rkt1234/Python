
# Polymorphism allows functions or methods to behave differently based on the object calling them.

class Dog:
    def speak(self):
        return "Bark"

class Cat:
    def speak(self):
        return "Meow"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())  # Polymorphic behavior
