'''Calculate the compound interest for a given principal amount, interest rate, and time period
The basic formula for compound interest is as follows:
At = A0(1 + r)**n

where:
A0 : principal amount, or initial investment
At : amount after time t
r : interest rate
n : number of compounding periods, usually expressed in years

'''
from example2 import validateUserInput

def main():
  principalAmount = validateUserInput("What's the principal amount: ")
  rate = validateUserInput("What's the interest rate: ")
  time = validateUserInput("What's the time period: ")

  print(f'${calculateCompoundInterest(principalAmount, rate, time):,}')


def calculateCompoundInterest(principalAmount, rate, time):
  return round((principalAmount * (1 + rate/100)**time), 2)


if __name__ == '__main__':
  main()