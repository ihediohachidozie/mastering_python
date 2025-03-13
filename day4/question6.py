"""Calculate the area of a triangle given its base and height using a function."""

from num_validation import validateUserInput

def main():
  base = float(validateUserInput('Enter the base: '))
  height = float(validateUserInput('Enter the height: '))
  print(f'Area of triangle = {calculateAreaOfTriangle(base, height)}')


def calculateAreaOfTriangle(base, height):
  return (0.5 * base * height)


if __name__ == '__main__':
  main()