# The map() is used to apply a function to each item of an iterable
# Syntax is below 
# map(function, iterable)
#  returns a map object, which is an iterator

nos = [1,2,3,4,5]

square = lambda a:a**2

print(list(map(square, nos)))