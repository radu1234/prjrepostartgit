from studentsapp.domain.entities import Teacher
from studentsapp.operations.studentoperations import StudentOperations
from studentsapp.ui.console import StudentConsole


#################entitati de domeniu#################################


#####################################################################


###########################operatii######################################


########################################################

######################## UI - citiri / afisari###########################


############################################################################

def main():
    # todo: try-except duplicate id

    student_operations = StudentOperations()
    console = StudentConsole(student_operations)

    console.add_student()
    console.add_student()
    console.print_students()

    # all_students = read_student_list()
    # print_students(all_students)
    #
    # student = read_student()
    # try:
    #     add_student(all_students, student.id, student.name, student.grade)
    #     print("student added successfully")
    # except ValueError as ve:
    #     print("Exception adding student: ", ve)
    # print_students(all_students)
    # print("bye")

    # t=Teacher()
    # print(t)
    # t=Teacher(1,"t1")
    # print(t.get_name())


main()
