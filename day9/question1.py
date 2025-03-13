"""
Create a class to represent a Student with attributes like 
name, age, and grades
"""
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades if grades is not None else []

    
    def __str__(self):
        return f"{self.name}, is {self.age} years old with grades {self.grades}"
    
    def add_grade(self, grade):
        if grade:
            self.grades.append(grade)
        return"Grade added successfully."
    
    def calculate_average(self):
        if not self.grades:
            return 0.0
        return sum(self.grades)/len(self.grades)

student1 = Student("Noel", 7, [88.5, 92.0])
student1.add_grade(80.5)
student1.add_grade(81.9)
print(student1)
print(f"{student1.name}'s average: {student1.calculate_average():.1f}")
