# A generator is a simpler way to create iterators using the yield keyword.
# In Python, the yield keyword is used to create generators, which are special types of iterators that allow values to be produced lazily, 
# one at a time, instead of returning them all at once. 
# This makes yield particularly useful for handling large datasets efficiently, as it allows iteration without storing the 
# entire sequence in memory.
def my_gen():
    yield 1
    yield 2
    yield 3

for i in my_gen():
    print(i)

# 🧠 Generators remember their state between yield calls and don’t store the entire sequence in memory — they’re memory efficient!
# It is used to generate values on the fly whenever needed. We do not need to generate all the values at once and keep it in a list