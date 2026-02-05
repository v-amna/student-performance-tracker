from dataclasses import dataclass

# This class represents a student with their name, gender, and scores in various subjects.
# The __str__ method is overridden to provide a readable string representation of the student object when printed.
# dataclass is used to automatically generate special methods like __init__ and __repr__, making it easier to create and manage student objects.
@dataclass
class Student:
    name:str
    gender:str
    english_score:float
    math_score:float
    science_score:float
    art_score:float
    
    def __str__(self):
        return f"Name: {self.name}| Gender: {self.gender}| English Score: {self.english_score}| Math Score: {self.math_score}| Science Score: {self.science_score}| Art Score: {self.art_score}"


# This class is a manager for student objects, to add,update,delete,view,search and filter students.
class StudentManager:

    # Dictionary to store student objects with their Id as the key.  
    students: dict[int, Student] = {} 

    # varible to keep track of the next student Id.
    next_id: int = 1


    # Method to add a new student and returns the assigned student Id.
    def add_student(self, student: Student) -> int:
        student_id = self.next_id
        self.students[student_id] = student
        self.next_id += 1
        return student_id
    
    # read student details from the user and create a new student object, then add it to the manager.
    # TODO: Add input validation 
    def create_student(self):
        name = input("Enter student name: ")
        gender = input("Enter student gender: ")
        english_score = float(input("Enter English score: "))
        math_score = float(input("Enter Math score: "))
        science_score = float(input("Enter Science score: "))
        art_score = float(input("Enter Art score: "))
        student = Student(name, gender, english_score, math_score, science_score, art_score)
        student_id = self.add_student(student)
        print(f"Student added with ID: {student_id}")

    # Method to list all students 
    def list_students(self):
        if not self.students:
            print("No students exist.")
            return
        for student_id, student in self.students.items():
            print(f"ID: {student_id} | {student}")
