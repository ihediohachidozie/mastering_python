"""Create a program that takes a year as input and checks if it is a leap year or not."""

from num_validation import validateUserInput

def main():
  year = validateUserInput('Enter a year: ')
  if isLaepYear(year):
    print(f'{year} is a leap year')
  else:
    print(f'{year} is not a leap year')


def isLaepYear(year):
  if year % 4 == 0:
    return True
  else:
    return False


if __name__ == '__main__':
  main()