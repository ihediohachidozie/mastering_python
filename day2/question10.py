#  Write a program to check if a number is prime.

from question2 import validateUserInput
def main():
  userInput = validateUserInput('Enter a number: ')
  if isPrimeNumber(userInput):
    print(f'{userInput} is a prime number')
  else:
    print(f'{userInput} is not a prime number')


def isPrimeNumber(number):
  for x in range(2, number):
    if number % x == 0:
      return False
  else:
    # loop fell through without finding a factor
    return True


if __name__ == '__main__':
  main()