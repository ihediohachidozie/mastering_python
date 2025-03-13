"""Create a program that generates the Fibonacci sequence up to a given number of terms."""

def main():
  fibonacci(10)


def fibonacci(counter):
  a, b = 0, 1
  while counter > 0:
    print(a, end=' ')
    a, b = b, a + b
    counter -= 1


if __name__ == '__main__':
  main()