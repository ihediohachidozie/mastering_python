"""Write a program that checks if a given number is positive, negative, or zero."""
from num_validation import validateUserInput

num = validateUserInput('Enter a number: ')

if num > 0:
  print(f'{num} is a positive number')
elif num < 0: 
  print(f'{num} is a negative number')
else:
  print(f'{num} is zero')