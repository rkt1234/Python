# *args and **kwargs are special syntaxes in Python used in function definitions to accept a variable number of arguments.

# ✅ *args (Non-keyword Variable-Length Arguments)
# Used to pass a variable number of positional arguments to a function.
# Inside the function, args is treated as a tuple.

def add_numbers(*args):
    print(args[2])  # args is a tuple
    return sum(args)

print(add_numbers(1, 2, 3, 4))  # Output: 10
