# Write a Python program to calculate the area of a rectangle given its length and width.
# **********************************************
# Formula => A = wl
# **********************************************

from example2 import validateUserInput

def main():
  print('To calculate the area of a rectangle (A = w * l)')
  print('*' * 50)
  print()
  length = validateUserInput('Enter the Length: ')
  width = validateUserInput('Enter the Width: ')
  print(f'Area = {area(width, length):.2f}')

def area(width, length) -> float:
  return width * length

if __name__ == '__main__':
  main()