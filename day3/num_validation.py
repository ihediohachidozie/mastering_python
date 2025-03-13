def main():
  pass

def validateUserInput(text):
  while True:
    try:
      return int(input(text))
    except ValueError:
      print('Oops!  That was no valid number.  Try again...')

if __name__ == '__main__':
  main()