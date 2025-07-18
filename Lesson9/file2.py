class Vehicle:
    def start(self):
        print("Starting the vehicle...")

class Car(Vehicle):
    def start(self):
        print("Starting the car...")

class Bike(Vehicle):
    def start(self):
        print("Starting the bike...")

for v in [Car(), Bike()]:
    v.start()

