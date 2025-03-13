# Create a function to count the number of vowels in a given string.

import re

def main():
  userInput = input('Enter the string: ').lower()
  print(countVowels(userInput))


def countVowels(myString):
  listOfVowels = re.findall('[aeoiu]', myString)
  return len(listOfVowels)


if __name__ == '__main__':
  main()