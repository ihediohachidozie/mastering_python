"""Create a function to find the square of each element in a given list."""
import numpy as np

def main():
  myList = [1,2,3,4]
  print(calculateSquareOfListElements(myList))
  print(square_elements(myList))


# Or
def square_elements(myList):
  arr = np.array(myList)
  print(arr ** 2)


def calculateSquareOfListElements(myList):
  return list(map(squared, myList))
  return ([x**2 for x in myList])

def squared(x):
  return x**2

if __name__ == '__main__':
  main()