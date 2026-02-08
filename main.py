from student import Student, StudentManager



studentmanager=StudentManager()
studentmanager.create_student()
studentmanager.list_students()
studentmanager.update_student(1)
studentmanager.list_students()
studentmanager.delete_student(1)
studentmanager.list_students()

sId=input("Enter student ID to search for: ")
studentmanager.search_student_by_id(int(sId))