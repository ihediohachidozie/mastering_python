"""Create a set of unique numbers from a list of numbers."""

def main():
  numbers = [1,2,3,3,1,4,5,2,3,7,6,7,8,9,2,1,1,6]
  uniqueNumbers = set(numbers)
  print(uniqueNumbers)


if __name__ == '__main__':
  main()