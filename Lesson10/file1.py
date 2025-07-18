# An iterator is an object that allows you to iterate over a sequence, like a list, tuple, or string.
# __iter__() returns the iterator object.
# __next__() returns the next item from the sequence.

my_list = [1, 2, 3]
iterator = iter(my_list)

print(iterator)
print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
# print(next(iterator))  # Raises StopIteration
