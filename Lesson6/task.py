# Write a calculator that catches division by zero and invalid inputs

def ad(a, b):
    return a + b

def sub(a, b):
    try:
        if a >= b:
            return a - b
        else:
            raise ValueError("Subtraction error: First value is smaller than the second.")
    except ValueError as e:
        print(e)

    finally:
        print("Operation completed")


def mul(a, b):
    return a * b

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except TypeError:
        print("Invalid input: Please enter numbers.")
    finally:
        print("Operation completed")

# --- Example Usage ---
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Choose operation (+, -, *, /): ")

    if op == '+':
        print("Result:", ad(a, b))
    elif op == '-':
        print("Result:", sub(a, b))
    elif op == '*':
        print("Result:", mul(a, b))
    elif op == '/':
        print("Result:", div(a, b))
    else:
        print("Invalid operation")

except ValueError:
    print("Invalid input: Please enter numeric values.")
