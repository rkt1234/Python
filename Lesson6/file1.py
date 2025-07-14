try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Execution complete")

# | Keyword   | Purpose                                 |
# | --------- | --------------------------------------- |
# | `try`     | Block of code to test                   |
# | `except`  | Handles the error                       |
# | `finally` | Executes no matter what (e.g., cleanup) |
# | `raise`   | Manually throw an exception             |
