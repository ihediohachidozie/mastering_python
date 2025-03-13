"""Given a list of numbers, create a function to find the sum of all positive numbers."""
def main():
  print(calculateSumOfList([1,2,3,-4]))


def calculateSumOfList(data):
  return sum(filter(is_positive, data))
  #return sum([x for x in data if x > 0])

def is_positive(x):
  if x > 0:
    return x

if __name__ == '__main__':
  main()