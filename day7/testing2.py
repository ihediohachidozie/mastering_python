# Create a dictionary that uses the departments as keys.
# Each key should map a list of people working in the department.

from collections import defaultdict

employees = [
  ('Sales', 'John'),
  ('Sales', 'Martin'),
  ('Accounting', 'Kate'),
  ('Marketing', 'Elizabath'),
  ('Marketing', 'Linda'),
]

departments = defaultdict(list)

for department, employee in employees:
  departments[department].append(employee)

print(departments['Accounting'])




