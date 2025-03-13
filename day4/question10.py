"""Create a function that takes a number as input and prints its multiplication table."""
from num_validation import validateUserInput

def main():
  print('Program to generate multiplication table of a given number')
  print('*'*60)
  userInput = validateUserInput('Enter a number: ')
  displayMultiplicationTable(userInput)


def displayMultiplicationTable(number):
  for x in range(1, 13):
    print(f'{number} * {x} = {number * x}')


if __name__ == '__main__':
  main()