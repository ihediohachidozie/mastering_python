"""Create a function to check if a number is prime."""

from num_validation import validateUserInput

def main():
  number = validateUserInput('Enter a number: ')

  if isPrimeNumber(number):
    print(f'{number} is a prime number')
  else:
    print(f'{number} is not a prime number')


def isPrimeNumber(number):
  for x in range(2, number):
    if number % x == 0:
      return False
  else:
    # loop fell through without finding a factor
    return True

    

if __name__ == '__main__':
  main()