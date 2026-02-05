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
        return f"Name: {self.name}, Gender: {self.gender}, English Score: {self.english_score}, Math Score: {self.math_score}, Science Score: {self.science_score}, Art Score: {self.art_score}"


    