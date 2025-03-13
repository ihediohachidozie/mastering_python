"""Implement a function that checks if a given string is a pangram (contains all letters of the alphabet)."""

def main():
  userInput = input('Enter a sentence: ')
  print(isPangram(userInput))


def isPangram(words):
  newText = words.replace(" ", '').lower()
  return True if len(set([x for x in newText])) == 26 else False


if __name__ == '__main__':
  main()
