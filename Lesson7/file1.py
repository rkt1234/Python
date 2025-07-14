# OOP allows you to:

# Bundle data + functions into reusable components (classes)

# Model real-world things (users, posts, models, APIs)

# Keep your code organized and maintainable

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"{self.brand} - {self.year}")

# Creating objects
my_car = Car("Toyota", 2020)
my_car.display_info()

