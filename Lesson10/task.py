# Write a generator function count_up_to(n) that yields numbers from 1 to n.
def count_up_to(n):
    for i in range (1,n+1):
        yield i 

print(next(count_up_to(5)))
print(next(count_up_to(5)))