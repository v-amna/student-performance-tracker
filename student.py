from dataclasses import dataclass
import json
from pathlib import Path


# This class represents a student with their name, gender, and scores in various subjects.
# The __str__ method is overridden to provide a readable string representation of the student object when printed.
# dataclass is used to automatically generate special methods like __init__ and __repr__, making it easier to create and manage student objects.
@dataclass
class Student:
    id:int
    name:str
    gender:str
    english_score:int = 0
    math_score:int = 0
    science_score:int = 0
    art_score:int = 0
    
    def __str__(self):
        return f"Id: {self.id} | Name: {self.name} | Gender: {self.gender} | English Score: {self.english_score} | Math Score: {self.math_score} | Science Score: {self.science_score} | Art Score: {self.art_score} | Total score: {self.total_score()}"

    # Method to calculate total score of the student by summing up the scores in all subjects.
    def total_score(self) -> int:
        return self.english_score + self.math_score + self.science_score + self.art_score
    
# This class is a manager for student objects, to add,update,delete,view,search and filter students.
class StudentManager:

    # Dictionary to store student objects with their Id as the key.  
    students: dict[int, Student] = {} 

    # varible to keep track of the next student Id.
    next_id: int = 1

    file_path: str = "students.json"


    # Method to add a new student and returns the assigned student Id.
    def add_student(self, student: Student) -> int:
        student_id = self.next_id
        student.id = student_id  # Assign the generated ID to the student object
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
    
    # Method to create student object from given dictionary
    def from_dict(self, data: dict) -> Student:
        return Student(
            id=data["id"] if "id" in data else 0,  # ID will be assigned when the student is added to the manager
            name=data["name"],
            gender=data["gender"],
            english_score=int(data["english_score"]),
            math_score=int(data["math_score"]),
            science_score=int(data["science_score"]),
            art_score=int(data["art_score"])
        )
    
    # Method to add a student from given dictionary, 
    # it creates a student object and adds it to the manager.
    def add_student_from_dict(self, data: dict) -> int:
        student = self.from_dict(data)
        return self.add_student(student)

    # read student details from the user and create a new student object, then add it to the manager.
    def create_student(self):
        print("Enter details for the new student:\n")
        student = self.from_dict(
            self.read_student_details())
        
        student_id = self.add_student(student)
        self._save()  # Save the updated students data to the JSON file after adding a new student
        print(f"Student added with ID: {student_id}")

    # Method to list all students 
    def list_students(self):
        if not self.students:
            print("No students exist.")
            return
        for student in self.students.values():
            print(f"{student}")
    
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
        student.english_score = int(updated_data["english_score"]) if  updated_data["english_score"] else student.english_score
        student.math_score = int(updated_data["math_score"]) if  updated_data["math_score"] else student.math_score
        student.science_score = int(updated_data["science_score"]) if  updated_data["science_score"] else student.science_score
        student.art_score = int(updated_data["art_score"]) if  updated_data["art_score"] else student.art_score
        print(f"Student with ID {student_id} has been updated.")
        self._save()  # Save the updated students data to the JSON file after updating a student

    # Method to delete a student by their Id
    def delete_student(self, student_id: int):
        """Deletes a student by their ID."""
        confirmation = input(f"Do you want to delete the student with ID {student_id}? (yes/no): ")
        if confirmation.lower() == "yes":
            if student_id in self.students:
                del self.students[student_id]
                print(f"Student with ID {student_id} has been deleted.")
                self._save()  # Save the updated students data to the JSON file after deleting a student
            else:
        
                print(f"Student with ID {student_id} does not exist.")
        else: 
            print("Deletion process canceled.")

    #Method to search for students by id 
    def search_student_by_id(self, student_id: int):
        """Searches for a student by their ID."""
   
        if student_id in self.students:
            print(f"ID: {student_id} | {self.students[student_id]}")
        else:
            print(f"Student with ID {student_id} does not exist.")

    # Method to create a json dump of students data
    def _save(self):
        """Saves the students data to a JSON file."""
        with open(self.file_path, 'w') as f:
            print(f"Saving students data to {self.file_path}...")       
            json.dump([student.__dict__ for student in self.students.values()] ,fp=f, indent=4)
            return
        print(f"Students data file save failed to save to {self.file_path}.")

    # Method to load students data from a json file
    def load(self,file_path: str = None):
        """Loads the students data from a JSON file."""
        self.file_path = file_path if file_path else self.file_path

        if not Path(self.file_path).exists():
            print(f"No existing data file found at {self.file_path}. Starting with an empty student manager.")
            return
        with open(self.file_path, 'r') as f:
            print(f"Loading students data from {self.file_path}...")
            students_data = json.load(f)
            for student_data in students_data:
                student = self.from_dict(student_data)
                self.students[student.id] = student
                self.next_id = max(self.next_id, student.id + 1)  # Ensure next_id is always greater than the highest existing ID

    #Method to filter students by Marks ,whose got distINCTION, FIRST CLASS, SECOND CLASS, THIRD CLASS and FAIL    
    