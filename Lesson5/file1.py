# A function is a reusable block of code that performs a specific task.
def greet():
    print("Hello, Ravikant!")

greet()  # Call the function

def greet(name):
    print(f"Hello, {name}!")

greet("Ravi")  # Hello, Ravi!

def add(a, b):
    return a + b

result = add(5, 7)
print(result)  # 12

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()          # Hello, Guest
greet("Gandu")    # Hello, Ravi
