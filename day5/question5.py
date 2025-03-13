"""Given a string, write a function to remove all vowels from it and return the modified strings."""

import re

def main():
  userInput = input('Enter a sentence: ')
  print(removeVowels(userInput))


def removeVowels(words):
  return re.sub('[a,e,i,o,u]', '', words)


if __name__ == '__main__':
  main()