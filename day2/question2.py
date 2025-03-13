# Create a program that takes a temperature in Clesius and converts it to Kelvin.


def main():
  print("""
  Temperature Conversion from
  ***************************
  1. Degree Celsius to Kelvin
  2. Kelvin to Degree Celsius 
  ***************************
  """)
  while True:
    userChoice = input('Select either 1 or 2: ')
    if userChoice == '1':
      print(calculateKelvin(validateUserInput('Enter a Temperature in Degree Celsius: ')))
      break
    elif userChoice == '2':
      print(calculateCelsius(validateUserInput('Enter a Temperature in Kelvin: ')))
      break
    else:
      print('Please enter either 1 or 2. Thank you.')


def validateUserInput(text):
  while True:
    try:
      return int(input(text))
    except ValueError:
      print('Oops!  That was no valid number.  Try again...')


def calculateKelvin(celsius):
  return f'{celsius + 273.15}K'


def calculateCelsius(kelvin):
  return f'{kelvin - 273.15}C'


if __name__ == '__main__':
  main()