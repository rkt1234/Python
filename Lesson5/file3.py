# ✅ **kwargs (Keyword Variable-Length Arguments)
# Used to pass a variable number of keyword arguments (i.e., named arguments).
# Inside the function, kwargs is treated as a dictionary.

def print_info(**kwargs):
    print(kwargs["name"])

print_info(name="Ravi", age=25, city="Delhi")
# Output: {'name': 'Ravi', 'age': 25, 'city': 'Delhi'}
