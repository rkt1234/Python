def sum_of_squares(n: int) -> int:
    return sum(i * i for i in range(1, n + 1))

def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def greet_user(name: str = "Guest") -> None:
    print(f"Hello, {name}!")
