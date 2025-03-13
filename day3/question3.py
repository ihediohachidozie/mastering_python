"""Write a Python program to check if a given number is a prime number."""
from num_validation import validateUserInput

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
    return True


if __name__ == '__main__':
  main()