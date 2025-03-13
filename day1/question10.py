"""Implement a program that swaps the values of two 
variables
"""

def main():
  firstNumber = 5
  secondNumber = 6
  firstNumber, secondNumber  = secondNumber, firstNumber
  print(firstNumber, secondNumber )


if __name__ == "__main__":
  main()