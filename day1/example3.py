# Convert temperature from Celsius to Fahrenheit.
# **********************************************
# Formula
# **********************************************
# Celsius to Fahrenheit => F = C * (9/5) + 32
# Fahrenheit to Celsius => C = (F - 32) * (5/9)

from example2 import validateUserInput

def main():
  print(f'The Temperature is {calculateTemperature()}')
  print('Thank you!')


def calculateTemperature()-> str:
  print('Temperature converter')
  print('*' * 40)
  print('1. Convert Celsius to Fahrenheit')
  print('2. Convert Fahrenheit to Celsius')
  print('*' * 40)
  print()
  while True:
    userChoice = input('Choose an option: ').strip()
    if userChoice == '2':
      fahrenheit = validateUserInput('Enter the Fahrenheit: ')
      return(f'{calculateCelsius(fahrenheit)} C')
    elif userChoice == '1':
      celsius = validateUserInput('Enter the Celsius: ')
      return(f'{calculateFahrenheit(celsius)} F')
    else:
      print('Enter either 1 or 2. Try agian')


def calculateCelsius(fahrenheit: float) -> float:
  return f'{(fahrenheit - 32) * (5/9):.2f}'


def calculateFahrenheit(celsius: float)-> float:
  return f'{(celsius * (9/5) + 32):.2f}'


if __name__ == '__main__':
  main()

