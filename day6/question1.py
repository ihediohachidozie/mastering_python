"""Given two list of numbers, concatenate them into a single list."""

def main():
  firstNumbers = [1,2,3,4,5]
  secondNumbers = [6,7,8,9,10]

  firstNumbers.extend(secondNumbers)

  print(firstNumbers)

  print([1,2,3,4,5] + [6,7,8,9,10])


if __name__ == '__main__':
  main()