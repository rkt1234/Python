def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18+")
    print("Access granted")

check_age(16)
