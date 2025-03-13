#  Write a Python program to check if a given string is a pangram (contains all letters of the alphabet).

def main():
  print('To check if a sentence is a pangram or not')
  userInput = input('Enter a sentence: ')
  if isPangram(userInput):
    print('It is a pangram')
  else:
    print('It is not a pangram') 

 
def isPangram(text):
  newText = text.replace(" ", '').lower()
  if len(set([x for x in newText])) == 26:
    return True
  else:
    return False


if __name__ == "__main__":
  main()