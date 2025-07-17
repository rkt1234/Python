class Vehicle:
    def __init__(self, name, max_speed):
        print("Parent class constructor is called")
        self.name = name 
        self.max_speed = max_speed
    
    def display_info(self):  # ⛔️ missing 'self'
        print(f"Vehicle Name: {self.name}, Max Speed: {self.max_speed} km/h")

class Car(Vehicle):
    def __init__(self, name, max_speed, fuel_type):
        super().__init__(name, max_speed)  # ⛔️ was missing args
        self.fuel_type = fuel_type
    
    def display_info(self):  # ✅ overriding
        print(f"Car Name: {self.name}, Max Speed: {self.max_speed} km/h, Fuel Type: {self.fuel_type}")

# 🔹 Example usage
c = Car("Honda City", 180, "Petrol")
c.display_info()
