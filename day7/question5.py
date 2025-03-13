"""Given a list of dictionaries, find the dictionary with the highest value for a specific key."""

def main():
  students = [
    {"name": "Eric", "age": 65, "major": "Literature"},
    {"name": "Alice", "age": 20, "major": "Computer Science"},
    {"name": "Bob", "age": 22, "major": "Mathematics"},
    {"name": "Charlie", "age": 19, "major": "Physics"},
    {"name": "John", "age": 45, "major": "Chemistry"},
    
  ]
  print(highest_dictionary(students))

  print(highest_dict(students))


def get_age(student):
  return student['age']


def highest_dictionary(students):
  """Find the dictionary with the highest value for a specific key.
  Args:
    students: A list of dictionaries.
  
  Returns:
    A dictionary with the hightest value.
  """
  # for student in sorted(students, key=lambda student: student['age'], reverse=True):
  for student in sorted(students, key=get_age, reverse=True):
    return student


def highest_dict(students):
  """Find the dictionary with the highest value for a specific key.
  Args:
    students: A list of dictionaries.
  
  Returns:
    A dictionary with the hightest value.
  """
  hightest = students[0]

  for student in students:
    if student['age'] > hightest['age']:
      hightest = student

  return hightest
  

if __name__ == '__main__':
  main()