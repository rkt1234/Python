# Create a numbers of 5 numbers. Print:

# First and last number

# Sorted numbers

# numbers in reverse

numbers = [1,100,69,-1,2]
print(numbers)

first_number = numbers[0]
last_number = numbers[-1]
print(first_number)
print(last_number)

numbers.sort()

print(numbers)

print(numbers[::-1])

# To-do list program:

# Start with an empty list

# Ask the user 3 times to input a task and add it to the list

# Print final to-do list

task=[]
for i in range(3):
    task1=input("Enter a task")
    task.append(task1)
print(task)


# Make a tuple of 3 cities

# Try accessing index 1

# Try modifying it and observe the error

cities = ("City1",("City2","City3"))
print(cities[0])
