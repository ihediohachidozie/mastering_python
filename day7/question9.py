"""Write a program that finds the average value of all the elements in a list of dictionaries."""

students = [
    {"name": "Alice", "age": 20, "major": "Computer Science"},
    {"name": "Bob", "age": 22, "major": "Mathematics"},
    {"name": "Charlie", "age": 19, "major": "Physics"},
    {"name": "John", "age": 45, "major": "Chemistry"},
    {"name": "Eric", "age": 65, "major": "Literature"}
]

sum_age = 0
for student in students:
  sum_age += student['age']

average_age = sum_age / len(students)
print(sum_age)
print(f'The average age is {average_age}')

# method 2 using map function

def get_age(student):
  return student['age']


sum_all = sum(map(get_age, students))
print(sum_all/len(students))