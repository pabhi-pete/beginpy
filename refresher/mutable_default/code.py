"""
Recommendation do not use default parameter values that are mutable!!!

"""
from typing import List, Optional

class Student:
    def __init__(self, name: str, grades: Optional[List[int]] = None) -> None:
        self.name = name
        self.grades = grades or []
    
    def take_exams(self, result: int):
        self.grades.append(result)

std1 = Student('std1')
std2 = Student('std2')
std1.take_exams([99,12,33,13])
print(std1.grades)
print(std2.grades)