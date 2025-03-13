""" Implement a function that takes a list of numbers and 
returns a new list with the squared values"""

import random

def main():
  my_list = random.sample(range(2, 10), 5)
  print(square_list_element(my_list))
  print(list(map(squared, my_list)))

def squared(x):
  return x**2

def square_list_element(numbers):
  """Square each elements in a list.
  Args:
    numbers: A list of numbers.
    
  Returns:
    A list of squared numbers.
  """
  return [x*x for x in numbers]


if __name__ == '__main__':
  main()