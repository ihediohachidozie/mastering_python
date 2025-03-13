# Write a program to check if a number is even or odd.

from example2 import validateUserInput

def main():
  number = validateUserInput('Enter a number: ')
  primeNumber(number)


def primeNumber(number):
  if number % 2 == 0:
    print('It is an even number')
  else:
    print('It is an odd number')


if __name__ == '__main__':
  main()