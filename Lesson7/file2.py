class Student:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

    def is_minor(self):
        return self.age < 18

s1 = Student(age=22)
print(s1.is_minor())  # False
