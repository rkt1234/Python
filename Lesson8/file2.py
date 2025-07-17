# super() is used to call the parent class’s constructor or methods from the child class.
class Parent:
    def intro(self):
        print("Mai hu parent")

class Child(Parent):
    def intro(self):
        super().intro()
        print("Mai hu child")


child = Child()
child.intro()