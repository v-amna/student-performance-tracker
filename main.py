from student import Student, StudentManager


studentmanager=StudentManager()
studentmanager.load('students.json')
# studentmanager.add_student_from_dict({"id":1, "name": "John Doe","gender": "Male","english_score": 85,"math_score": 90,"science_score": 80,"art_score": 34})
# studentmanager.add_student_from_dict({"id":2, "name": "Chakka","gender": "Male","english_score": 85,"math_score": 90,"science_score": 80,"art_score": 67})
# studentmanager.add_student_from_dict({"id":3, "name": "Doe D","gender": "Male","english_score": 34,"math_score": 43,"science_score": 56,"art_score": 9})
# studentmanager.add_student_from_dict({"id":4, "name": "Ela F","gender": "Female","english_score": 76,"math_score": 76,"science_score": 89,"art_score": 45})
studentmanager.list_students()
print("="*50)
# studentmanager.create_student()
# studentmanager.update_student(1)
# studentmanager.list_students()
# studentmanager.delete_student(1)
# studentmanager.list_students()

# sId=input("Enter student ID to search for: ")
# studentmanager.search_student_by_id(int(sId))