# Inheritance allows a class (child) to inherit properties and behavior from another class (parent).
class Parent:
    def speak(self):
        print("Parent speaking")

class Child(Parent):
    def walk(self):
        print("Child walking")

c = Child()
c.speak()   # Inherited
c.walk()    # Own method
