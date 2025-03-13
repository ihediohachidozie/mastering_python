"""Implement a program that reads a text file and counts the number of words and lines in it."""
from collections import Counter
import sys

def main():

  if len(sys.argv) > 1:
    total_words = number_of_words_lines(sys.argv[1])[0]
    total_lines = number_of_words_lines(sys.argv[1])[1]

    print(f'Total Words: {total_words} and Total Lines: {total_lines}')
    print(f'The text file has a {total_words} words and {total_lines} lines.')
  else:
    sys.exit('No file to read.')


def number_of_words_lines(file):
  """Count the number of words and lines

  Arg:
    file: The text file to count the contents
  
  Returns:
    The number of words and lines.
  """
  try:

    with open(f'{file}', 'r') as reader:
      number_of_words = Counter((reader.read()).split()).total()
      reader.seek(0)
      number_of_lines = len(reader.readlines())
  except:
    sys.exit('Something went wrong.')


  return number_of_words, number_of_lines


if __name__=='__main__':
  main()