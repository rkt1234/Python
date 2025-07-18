# reduce() used to reduce a list to a single value by applying a function cumulatively. You need to import it: from functools import reduce
# Syntax is below
# reduce(function, iterable)

from functools import reduce

nums = [1, 2, 3, 4]
sum = lambda x, y: x + y
sum_all = reduce(sum, nums)
print(sum_all)  # Output: 10
