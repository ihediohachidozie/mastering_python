"""Given a list of names, count the number of names that start with a vowel."""

import re

def main():
  names = ['John', 'Doe', 'Paul', 'Obi', 'Julian', 'Juan']
  print(countVowels(names))

  print(sum(list(map(count_vowels, names))))


def count_vowels(name):
  listOfVowels = re.findall('[aeoiu]', name.lower())
  return len(listOfVowels)



def countVowels(names):
  """Count the number of vowels in each name"""
  sumOfVowels = 0
  for name in names:
    listOfVowels = re.findall('[aeoiu]', name.lower())
    sumOfVowels += len(listOfVowels)
  return sumOfVowels


if __name__ == '__main__':
  main()