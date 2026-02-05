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
    
    # Method to create a new student by reading user input.
    # It returns student objects
    # TODO: Add input validation 
    def read_student_details(self) -> dict:
        name = input("Enter student name: ")
        gender = input("Enter student gender: ")
        english_score = input("Enter English score: ")
        math_score = input("Enter Math score: ")
        science_score = input("Enter Science score: ")
        art_score = input("Enter Art score: ")
        return {
            "name": name,
            "gender": gender,
            "english_score": english_score,
            "math_score": math_score,
            "science_score": science_score,
            "art_score": art_score
        }
    
    # Method to create student object from given dict
    def from_dict(self, data: dict) -> Student:
        return Student(
            name=data["name"],
            gender=data["gender"],
            english_score=data["english_score"],
            math_score=data["math_score"],
            science_score=data["science_score"],
            art_score=data["art_score"]
        )
    
    # read student details from the user and create a new student object, then add it to the manager.
    def create_student(self):
        print("Enter details for the new student:\n")
        student = self.from_dict(
            self.read_student_details())
        
        student_id = self.add_student(student)
        print(f"Student added with ID: {student_id}")

    # Method to list all students 
    def list_students(self):
        if not self.students:
            print("No students exist.")
            return
        for student_id, student in self.students.items():
            print(f"ID: {student_id} | {student}")
    
    # Method to Update by student Id
    def update_student(self, student_id: int):
        print("Enter new details for the student (leave blank to keep current value):\n")
        if student_id not in self.students:
            print(f"Student with ID {student_id} does not exist.")
            return
        
        updated_data = self.read_student_details()
        student = self.students[student_id]
    
        # Update only the fields that are provided if not empty
        student.name = updated_data["name"] if  updated_data["name"] else student.name
        student.gender = updated_data["gender"] if  updated_data["gender"] else student.gender
        student.english_score = updated_data["english_score"] if  updated_data["english_score"] else student.english_score
        student.math_score = updated_data["math_score"] if  updated_data["math_score"] else student.math_score
        student.science_score = updated_data["science_score"] if  updated_data["science_score"] else student.science_score
        student.art_score = updated_data["art_score"] if  updated_data["art_score"] else student.art_score
        print(f"Student with ID {student_id} has been updated.")