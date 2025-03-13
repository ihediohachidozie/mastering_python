"""Implement a function that returns the factorial of a given number using recursion."""
from num_validation import validateUserInput

def main():
  userInput = validateUserInput('Enter a number: ')
  if userInput >= 0:
    print(f'Factorial of {userInput} is {factorial(userInput)}')
  else:
    print('The factorial function is define for non-negative integers')


def factorial(n):
  return n * factorial(n - 1) if (n > 1) else 1


if __name__ == '__main__':
  main()
