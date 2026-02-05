from student import Student, StudentManager



studentmanager=StudentManager()
studentmanager.create_student()
studentmanager.list_students()
studentmanager.update_student(1)
studentmanager.list_students()
studentmanager.delete_student(1)
studentmanager.list_students()