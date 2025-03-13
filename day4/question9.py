"""Implement a function to check if a given year is a leap year or not."""
from num_validation import validateUserInput

def main():
  year = validateUserInput('Enter a year: ')
  if calculateLeapYear(year):
    print(f'{year} is a leap year')
  else:
    print(f'{year} is not a leap year')



def calculateLeapYear(year):
  if year % 4 == 0:
    return True
  else:
    return False



if __name__ == '__main__':
  main()