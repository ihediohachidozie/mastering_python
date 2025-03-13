# Calculate the sum of two numbers entered by the user.
def main():

  num1 = validateUserInput('Enter the first number: ')

  num2 = validateUserInput('Enter the second number: ')

  print(f'The sum of {num1} + {num2} = {num2 + num1}')

def validateUserInput(text: str) -> float:
  while True:
    try:
      num = float(input(text))
      return num
    except ValueError:
      print('You have entered an invalid number. Try again')

if __name__ == '__main__':
  main()