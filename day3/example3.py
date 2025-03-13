"""Implement a program that finds the largest number in a list."""

def main():
  print(f'The largest Value = {islargest([1,2,3,4])}')
  print(f'The Largest Value = {max([1,2,3,4])}')


def islargest(myList):
  largestValue = 0
  for x in myList:
    if x > largestValue:
      largestValue = x

  return largestValue


if __name__ == '__main__':
  main()
