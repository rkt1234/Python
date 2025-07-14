try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("You must enter an integer.")
except ZeroDivisionError:
    print("Zero is not allowed.")
