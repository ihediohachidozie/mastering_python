"""Write a program that finds the largest and smallest elements in a list."""
import random

def main():
  my_list = random.sample(range(100), 10)

  print(max(my_list))
  print(min(my_list))

  print(find_largest(my_list))
  print(find_smallest(my_list))

def find_largest(numbers):
  """Finds the largest number in a list.
  Args:
    numbers: A list of numbers.
    
  Returns:
    The largest number in the list.
  """
  if not numbers:
    return None
  
  largest = numbers[0]

  for number in numbers:
    if number > largest:
      largest = number
  
  return largest


def find_smallest(numbers):
  """Finds the smallest number in a list.
  Args:
    numbers: A list of numbers.
    
  Returns:
    The smallest number in the list.
  """
  if not numbers:
    return None
  
  smallest = numbers[0]

  for number in numbers:
    if number < smallest:
      smallest = number
  
  return smallest

if __name__ == '__main__':
  main()