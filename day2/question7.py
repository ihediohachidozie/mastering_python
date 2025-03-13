# Calculate the area and circumference of a circle given its radius.
# Area = pi * r**2
# C = 2 * pi * r

from math import pi
from question2 import validateUserInput

def main():
  print(""" 
    Calculate the following
    ***************************
    1. Area of a circle
    2. Circumference of a circle 
    ***************************
    """)
  
  while True:
    userChoice = input('Select either 1 or 2: ')
    match userChoice:
      case '1':
        print(f'{areaOfCirle(validateUserInput("Enter a the radius: ")):.2f}')
        break
      case '2':
        print(f'{circumference(validateUserInput("Enter a the radius: ")):.2f}')
        break
      case _:
        print('Please enter either 1 or 2. Try again.')
        


def areaOfCirle(radius):
  return pi * (radius**2)

def circumference(radius):
  return 2 * pi * radius

if __name__ == '__main__':
  main()