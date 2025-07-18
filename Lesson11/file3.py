# Filters the elements based on a condition (returns only items where the function returns True).
# Syntax is below 
# filter(function, iterable)
#  returns a filter object, which is an iterator

nos = [-1,-2,5,199,0,-4,-6]
check = lambda a: a>0
result = filter(check, nos)
print(list(result))
