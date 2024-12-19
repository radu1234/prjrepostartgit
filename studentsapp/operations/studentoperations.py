from studentsapp.domain.entities import Student


# def find_by_id(all_students, id):
#     for student in all_students:
#         if student.id == id:
#             return student
#     return None
#
#
# def add_student(all_students, id, name, grade):
#     if find_by_id(all_students, id) is not None:
#         raise ValueError('Student with id {} already exists'.format(id))
#     new_student = Student(id, name, grade)
#     all_students.append(new_student)


class StudentOperations:
    def __init__(self):
        self.__all_students = []

    def get_all_students(self):
        return self.__all_students

    def __find_by_id(self, id):
        for student in self.__all_students:
            if student.id == id:
                return student
        return None

    def add_student(self, id, name, grade):
        if self.__find_by_id(id) is not None:
            raise ValueError('Student with id {} already exists'.format(id))
        new_student = Student(id, name, grade)
        self.__all_students.append(new_student)
