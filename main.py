from unicodedata import category
from student import Student, StudentManager

class App:
    """Terminal-based student performance tracker application."""
    MENU = """
╔════════════════════════════════════════╗
║       Student Management System        ║
╠════════════════════════════════════════╣
║  1. List all students                  ║
║  2. Add new student                    ║
║  3. Update student                     ║
║  4. Delete student                     ║
║  5. Search students by ID              ║
║  6. Filter by Marks                    ║
║  7. Import from JSON file              ║     
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
                self.student_manager.create_student()
            elif choice == "3":
                try:
                    student_id = int(input("Enter student ID to update: "))
                    self.student_manager.update_student(student_id)
                except ValueError:
                    print("Invalid input. Please enter a valid integer ID.")
            elif choice == "4":
                try:
                    student_id = int(input("Enter student ID to delete: "))
                    self.student_manager.delete_student(student_id)
                except ValueError:
                    print("Invalid input. Please enter a valid integer ID.")
            elif choice == "5":
                try:
                    student_id = int(input("Enter student ID to search for: "))
                    self.student_manager.search_student_by_id(student_id)
                except ValueError:
                    print("Invalid input. Please enter a valid integer ID.")
            elif choice == "6":
                category = input("Enter category to filter students by (first class, second class, third class, fail): ")
                self.student_manager.filter_students_by_marks(category)
            elif choice == "7":
                filename = input("Enter the filename to import from (e.g., students.json): ")
                self.student_manager.load(filename)
            else:
                print("Invalid choice. Please try again.")
            
            print("\n" + "="*50 + "\n")
            input("Press Enter to continue...")
            choice = self._display_menu()

if __name__ == "__main__":
    # Run the application
    App().run()