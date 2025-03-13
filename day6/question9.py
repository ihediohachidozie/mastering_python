"""Write a program that checks if a given list is sorted in ascending order."""
import random
def main():
  numbers = random.sample(range(100), 10)
  print(is_sorted(numbers))
  print(is_sorted(sorted(numbers)))


def is_sorted(numbers):
  """Check if sorted in ascending order using built-in function ALL
  Args:
    numbers: A list of numbers
  
    Returns:
      A sorted list of numbers
  """
  return all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))
  # return myList == sorted(myList, reverse=True)
  # print(all(a[i] >= a[i + 1] for i in range(len(a) - 1))) # descending


if __name__ == '__main__':
  main()