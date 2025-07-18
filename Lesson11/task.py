# Write a lambda function to cube a number.

cube = lambda x:x*x*x
print(cube(2))

# Use map() to convert a list of temperatures in Celsius to Fahrenheit.
temp_in_celcius = [20,30,40]
temp_in_fahrenheit = []
convert = lambda x: (9*x+160)/5
temp_in_fahrenheit = list(map(convert, temp_in_celcius))
print(temp_in_fahrenheit)

# Use filter() to get only numbers greater than 10 from a list.
nos = [1,2,14,10,15,20]
check = lambda x: x>10
result = list(filter(check,nos))
print(result)

# Use reduce() to multiply all elements in a list.
from functools import reduce
mul = lambda x,y:x*y
ans=reduce(mul,nos)
print(ans)