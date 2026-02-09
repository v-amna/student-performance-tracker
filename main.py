from unicodedata import category
from student import Student, StudentManager

class App:
    """Terminal-based student performance tracker application."""
    MENU = """
╔════════════════════════════════════════╗
║       Student Management System        ║
╠════════════════════════════════════════╣
║  1. List all students                  ║
║  2. View student details               ║
║  3. Add new student                    ║
║  4. Update student                     ║
║  5. Delete student                     ║
║  6. Search students by ID              ║
║  7. Filter by Marks                    ║
║  8. Import from JSON file              ║     
║  0. Exit                               ║
║                                        ║
║                                        ║
╚════════════════════════════════════════╝
"""

    def __init__(self):
        self.student_manager = StudentManager()
        self.student_manager.load('students.json')  # Load students data from JSON file at startup

    def _display_menu(self):
        print(self.MENU)
        choice = input("Enter your choice: ")
        return choice
    
    def run(self):
        choice = self._display_menu()
        while choice != "0":
            if choice == "1":
                print("\n" + "="*50 + "\n")
                self.student_manager.list_students()
            elif choice == "2":
                student_id = int(input("Enter student ID to view details: "))
                self.student_manager.view_student_details(student_id)
            elif choice == "3":
                self.student_manager.create_student()
            elif choice == "4":
                student_id = int(input("Enter student ID to update: "))
                self.student_manager.update_student(student_id)
            elif choice == "5":
                student_id = int(input("Enter student ID to delete: "))
                self.student_manager.delete_student(student_id)
            elif choice == "6":
                student_id = int(input("Enter student ID to search for: "))
                self.student_manager.search_student_by_id(student_id)
            elif choice == "7":
                category = input("Enter category to filter students by (first class, second class, third class, fail): ")
                self.student_manager.filter_students_by_marks(category)
            elif choice == "8":
                filename = input("Enter the filename to import from (e.g., students.json): ")
                self.student_manager.load(filename)
            else:
                print("Invalid choice. Please try again.")
            
            print("\n" + "="*50 + "\n")
            choice = self._display_menu()

# Run the application
App().run()

# studentmanager.load('students.json')
# # studentmanager.add_student_from_dict({"id":1, "name": "John Doe","gender": "Male","english_score": 85,"math_score": 90,"science_score": 80,"art_score": 34})
# # studentmanager.add_student_from_dict({"id":2, "name": "Chakka","gender": "Male","english_score": 85,"math_score": 90,"science_score": 80,"art_score": 67})
# # studentmanager.add_student_from_dict({"id":3, "name": "Doe D","gender": "Male","english_score": 34,"math_score": 43,"science_score": 56,"art_score": 9})
# # studentmanager.add_student_from_dict({"id":4, "name": "Ela F","gender": "Female","english_score": 76,"math_score": 76,"science_score": 89,"art_score": 45})
# studentmanager.list_students()
# print("="*50)
# display_menu=studentmanager.display_menu()
# studentmanager.create_student()

# studentmanager.update_student(1)
# # studentmanager.list_students()
# studentmanager.delete_student(1)
# # studentmanager.list_students()

# sId=input("Enter student ID to search for: ")
# studentmanager.search_student_by_id(int(sId))
# category=input("Enter category to filter students by (first class, second class, third class, fail): ")
# studentmanager.filter_students_by_marks(category)