from studentsapp.domain.entities import Student
from studentsapp.operations.studentoperations import StudentOperations


# def read_student():
#     id = int(input("Enter student ID: "))
#     name = input("Enter student name: ")
#     grade = int(input("Enter student grade: "))
#     return Student(id, name, grade)
#
#
# def read_student_list():
#     students = []
#     nr = int(input("Enter student number: "))
#     for i in range(nr):
#         students.append(read_student())
#     return students
#
#
# def print_students(students):
#     print("\nStudents:")
#     if len(students) == 0:
#         print("No students")
#     else:
#         print(students)

class StudentConsole:

    # def __init__(self):
    #     self.__student_operations = StudentOperations()

    def __init__(self, student_operations):
        self.__student_operations = student_operations

    def add_student(self):
        id = int(input("Enter student ID: "))
        name = input("Enter student name: ")
        grade = int(input("Enter student grade: "))
        # return Student(id, name, grade)

        # student_operations=StudentOperations()
        # student_operations.add_student(id, name, grade)
        self.__student_operations.add_student(id, name, grade)

    def print_students(self):
        students=self.__student_operations.get_all_students()

        print("\nStudents:")

        if len(students) == 0:
            print("No students")
        else:
            print(students)
