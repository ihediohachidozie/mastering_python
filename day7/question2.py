"""Write a program that finds the most frequent element in a list."""

import statistics, numpy

def main():
  my_list = ['orange', 'grape', 'kiwi', 'kiwi', 'lemon', 'apple', 'mango', 'apple', 'apple']
  print(statistics.mode(my_list))


if __name__ == '__main__':
  main()