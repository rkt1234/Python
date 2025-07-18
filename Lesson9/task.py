# Write two classes — Bird and Fish — both with a method move() that prints flying/swimming respectively. Use a loop to call them.

class Bird:
    def __init__(self):
        pass

    def move(self):
        print("Flying")

# Write two classes — Bird and Fish — both with a method move() that prints flying/swimming respectively. Use a loop to call them.

class Fish:
    def __init__(self):
        pass

    def move(self):
        print("Swimming")

object_list = [Bird(), Fish()]

for object in object_list:
    object.move()

# Define an abstract class Appliance with an abstract method operate(). Implement two classes: WashingMachine and Refrigerator.

from abc import ABC, abstractmethod

class Appliance(ABC):
    @abstractmethod
    def operate(self):
        pass

class WashingMachine(Appliance):
    def operate(self):
        print("Operating Washing Machine")

class Refrigerator(Appliance):
    def operate(self):
        print("Operating Refrigerator")

washing_machine = WashingMachine()
refrigerator = Refrigerator()

washing_machine.operate();
refrigerator.operate()