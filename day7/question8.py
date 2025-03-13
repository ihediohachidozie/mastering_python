"""Create a function that takes a list of dictionaries and sorts them based on a specified key."""

def main():
  students = [
      {"name": "James", "age": 85, "major": "Geography"},
      {"name": "Alice", "age": 20, "major": "Computer Science"},
      {"name": "Bob", "age": 22, "major": "Mathematics"},
      {"name": "Charlie", "age": 19, "major": "Physics"},
      {"name": "John", "age": 45, "major": "Chemistry"},
      {"name": "Eric", "age": 65, "major": "Literature"},
      
  ]

  sort_dictionary(students)



def get_name(student):
  return student['name']


def sort_dictionary(students):
  """Sort list of dictionaries based on a specific key.
  Args:
    students: A list of dictionaries.
  
  Returns:
    A list of sorted dictionaries.
  """
  # for student in sorted(students, key=lambda student: student['name']):
  for student in sorted(students, key=get_name):
    print(student)


if __name__ == '__main__':
  main()