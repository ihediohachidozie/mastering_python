"""Implement a program that prints the multiplication table of a given number."""
from num_validation import validateUserInput

print('Program to generate multiplication table of a given number')
print('*'*60)
number = validateUserInput('Enter a number: ')

for x in range(1, 13):
  print(f'{number} * {x} = {number * x}')
