"""Write a program that calculates the factorial of a given number"""
from num_validation import validateUserInput

def main():
  number = validateUserInput('Enter a number: ')
  print(f'Factorial of {number} is {factorial(number)}')


def factorial(n):
  fact = 1
  while n > 0:
    fact *= n
    n -= 1
  return fact 


if __name__ == '__main__':
  main()
