class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

class GradeManager:
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        student = Student(name)
        self.students[name] = student

    def add_grade_to_student(self, name, grade):
        if name in self.students:
            self.students[name].add_grade(grade)
        else:
            print("Student not found.")

    def display_student_averages(self):
        for name, student in self.students.items():
            print(f"{name}: Average Grade = {student.calculate_average():.2f}")

# Example usage
manager = GradeManager()
manager.add_student("talha")
manager.add_grade_to_student("talha", 85)
manager.add_grade_to_student("talha", 92)
manager.add_student("ab")
manager.add_grade_to_student("ab", 78)
manager.display_student_averages()
