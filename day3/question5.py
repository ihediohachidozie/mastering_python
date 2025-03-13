"""Given a list of names, print all names starting with the letter 'A' """

import re

def main():
  print(startsWithA(['Alex', 'Matt', 'Abel', 'Angel', 'Noe', 'Doe', 'John']))


def startsWithA(myList):
  names = ' '.join(myList)
  namesStartWithA = re.findall('A\w+', names)
  return namesStartWithA
  #return [name for name in names if name.startswith('A')]


if __name__ == '__main__':
  main()