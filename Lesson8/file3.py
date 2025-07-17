# When a child class defines a method with the same name as the parent class, the child’s method overrides the parent’s.
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):     # Overriding
        print("Dog barks")

d = Dog()
d.sound()  # "Dog barks"

