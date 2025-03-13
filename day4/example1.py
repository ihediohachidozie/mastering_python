"""Write a function to calculate the area of a circle given its radius."""
from math import pi
from num_validation import validateUserInput

def main():
  print(""" 
    Calculate the following
    ***************************
    1. Area of a circle
    2. Circumference of a circle 
    ***************************
    """)
  while True:
    user_request = input('Select either 1 or 2: ')
    if user_request == '1':
      print(f'{calculateAreaOfCirle(validateUserInput("Enter a the radius: ")):4f}')
      break
    elif user_request == '2':
      print(f'{calculateCircumference(validateUserInput("Enter a the radius: ")):4f}')
      break
    else:
      print('Please enter either 1 or 2. Try again.')


def calculateAreaOfCirle(radius):
  return pi * (radius**2)


def calculateCircumference(radius):
  return 2 * pi * radius


if __name__ == '__main__':
  main()