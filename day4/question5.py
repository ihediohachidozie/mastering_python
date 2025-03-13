"""Write a function to check if a number is even or odd and return 'Even' or 'Odd' accordingly."""

from num_validation import validateUserInput

def main():
  userInput = validateUserInput('Enter a number: ')
  if isEvenOdd(userInput):
    print('Even')
  else:
    print('Odd')


def isEvenOdd(number):
  if number % 2 == 0:
    return True
  else:
    return False


if __name__ == '__main__':
  main()