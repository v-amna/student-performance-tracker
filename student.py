from dataclasses import dataclass


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


    