"""Create a loop that prints all prime numbers between 1 and 50."""

def main():
  startValue = 1
  endValue = 50
  #isPrimeNumber(startValue, endValue)
  print(list(filter(is_prime, range(startValue, endValue))))


def isPrimeNumber(start, end):
  for num in range(start, end + 1):
    for x in range(2, num):
      if num % x == 0:
        break
    else:
      print(num, end=' ')

def is_prime(x):
  if x != 1 and x % 2 != 0:
    return x
  




if __name__ == '__main__':
  main()
