class Student:
    list_of_students=[]
    def __init__(self,name,roll_no,maths,physics,chemistry) -> None:
        self.name=name
        self.roll_no=roll_no
        self.physics=physics
        self.chemistry=chemistry
        self.maths=maths

    @staticmethod
    def display_all_students():
        for student in Student.list_of_students:
            print(student.name)
    
    @staticmethod
    def search_student(roll_no) -> None:
        for student in Student.list_of_students:
            if student.roll_no == roll_no:
                print("Student found")
                return None
        
        print("Does not exist")
        return None
    
    @staticmethod
    def calculate_average_marks():
        marks=0
        for student in Student.list_of_students:
            marks = marks + student.physics + student.chemistry + student.maths
        
        avg = marks/len(Student.list_of_students)
        print(f"The average is {avg}")

    @staticmethod
    def topper():
        if not Student.list_of_students:
            print("No students available")
            return

        top_student = None
        max_marks = -1

        for student in Student.list_of_students:
            total = student.physics + student.chemistry + student.maths
            if total > max_marks:
                max_marks = total
                top_student = student

        print(f"Topper is {top_student.name} with total marks {max_marks}")


