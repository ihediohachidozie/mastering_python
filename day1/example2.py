# Calculate the sum of two numbers entered by the user.
def main():
  firstNumber = validateUserInput('Enter the first number: ')
  secondNumber = validateUserInput('Enter the second number: ')
  print(f'The sum of {firstNumber} + {secondNumber} = {secondNumber + firstNumber}')


def validateUserInput(text: str) -> float:
  while True:
    try:
      userInput = float(input(text))
      return userInput
    except ValueError:
      print('Oops!  That was no valid number.  Try again...')


if __name__ == '__main__':
  main()