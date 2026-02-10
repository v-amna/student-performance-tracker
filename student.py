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
        """Calculates the total score of the student by summing up the scores in all subjects."""
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
        """Adds a new student to the manager and returns the assigned student ID."""
        student_id = self.next_id
        student.id = student_id  # Assign the generated ID to the student object
        self.students[student_id] = student
        self.next_id += 1
        return student_id
    
    # Method to validate given user input is a valid full name
    # It checks if the name is not empty and contains at least two parts (first name and last name).

    def _validate_name(self, name: str, allow_empty: bool=False) -> bool:
        """Validates that the name is a valid full name (first and last name) or empty if allow_empty is True."""
        if not name.strip():
            return allow_empty
    
        parts = name.split()
        return len(parts) >= 2
    
    # Method to validate given user input is either Male, Female
    # Or it's empty when allow_empty is set to True on update to skip

    def _validate_gender(self, gender: str, allow_empty: bool=False) -> bool:
        """Validates that the gender is either 'Male' or 'Female' or empty if allow_empty is True."""
        if not gender.strip():
            return allow_empty
        return gender.lower() in ["male", "female"]
    
    # Method to validate give user input is a valid score, 
    # which is an integer between 0 and 100, or it's empty when allow_empty is set to True.

    def _validate_score(self, score: str, allow_empty: bool=False) -> bool:
        """Validates that the score is an integer between 0 and 100 or empty if allow_empty is True."""
        if not score.strip():
            return allow_empty
        if not score.isdigit():
            return False
        value = int(score)
        return 0 <= value <= 100

    # Method to readinput with given prompt unitl a valid input is provided, 
    # it uses the provided validation function to check the validity of the input 
    # and displays the given error message if the input is invalid.

    def _read_validated_input(self, prompt: str, validation_func, error_message: str, allow_empty: bool=False) -> str:
        """Reads input from the user with validation."""
        while True:
            user_input = input(prompt)
            if validation_func(user_input, allow_empty=allow_empty):
                return user_input
            print(error_message)

    # Method to create a new student by reading user input.
    # It returns student objects

    def read_student_details(self,is_update=False) -> dict:
        """Reads student details from user input and returns a dictionary of the details."""
        
        name = self._read_validated_input(
                prompt="Enter student name: ", 
                validation_func=self._validate_name, 
                error_message="Invalid name. Please enter a valid full name (first and last name).", 
                allow_empty=is_update
            )        
        gender = self._read_validated_input(
                prompt="Enter student gender: ",
                validation_func=self._validate_gender,
                error_message="Invalid gender. Please enter 'Male' or 'Female'.",
                allow_empty=is_update
            )
        english_score = self._read_validated_input(
                prompt="Enter English score: ",
                validation_func=self._validate_score,
                error_message="Invalid score. Please enter an integer between 0 and 100.",
                allow_empty=is_update
            )
        math_score = self._read_validated_input(
                prompt="Enter Math score: ",
                validation_func=self._validate_score,
                error_message="Invalid score. Please enter an integer between 0 and 100.",
                allow_empty=is_update
            )
        science_score = self._read_validated_input(
                prompt="Enter Science score: ",
                validation_func=self._validate_score,
                error_message="Invalid score. Please enter an integer between 0 and 100.",
                allow_empty=is_update
            )
        art_score = self._read_validated_input(
                prompt="Enter Art score: ",
                validation_func=self._validate_score,
                error_message="Invalid score. Please enter an integer between 0 and 100.",
                allow_empty=is_update
            )
        
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
        """Creates a Student object from a dictionary of student details."""
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
        """Adds a student to the manager from a dictionary of student details and returns the assigned student ID."""
        student = self.from_dict(data)
        return self.add_student(student)

    # read student details from the user and create a new student object, then add it to the manager.

    def create_student(self):
        """Creates a new student by reading details from user input and adds it to the manager."""
        print("Enter details for the new student:\n")
        student = self.from_dict(
            self.read_student_details())
        
        student_id = self.add_student(student)
        self._save()  # Save the updated students data to the JSON file after adding a new student
        print(f"Student added with ID: {student_id}")

    # Method to list all students 

    def list_students(self):
        """Lists all students in the manager."""
        if not self.students:
            print("No students exist.")
            return
        for student in self.students.values():
            print(f"{student}")
    
    # Method to Update by student Id

    def update_student(self, student_id: int):
        """Updates a student by their ID."""
        print("Enter new details for the student (leave blank to keep current value):\n")
        if student_id not in self.students:
            print(f"Student with ID {student_id} does not exist.")
            return
        updated_data = self.read_student_details(is_update=True)
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
        print("Student details updated successfully.")

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
        if not isinstance(student_id, int):
            print("Invalid ID. Please enter a valid integer ID.")
            return
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
                self.next_id = max(self.next_id, student.id + 1)  # confirm next_id is always greater than the highest existing ID

    #Method to filter students by Marks ,whose got DISINCTION, FIRST CLASS, SECOND CLASS, THIRD CLASS and FAIL    

    def filter_students_by_marks(self, category: str):
        """Filters students by their marks category."""
        category = category.lower()
        filtered_students = []
        for student in self.students.values():
            total_score = student.total_score()
            if category == "distinction" and total_score >= 380:
                filtered_students.append(student)
            elif category == "first class" and 300 <= total_score < 380:
                filtered_students.append(student)
            elif category == "second class" and 240 <= total_score < 300:
                filtered_students.append(student)
            elif category == "third class" and 180 <= total_score < 240:
                filtered_students.append(student)
            elif category == "fail" and total_score < 180:
                filtered_students.append(student)

        if not filtered_students:
            print(f"No students found in the '{category}' category.")
        else:
            print(f"Students in the '{category}' category:")
            for student in filtered_students:
                print(student)   

