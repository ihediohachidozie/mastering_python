"""Write a Python program to find the length of the longest word in a sentences."""

def main():
  userInput = input('Enter the sentence: ')
  print(findLongestWord(userInput))


def findLongestWord(sentence):
  """Finds the longest word in a given sentence."""
  words = sentence.split()
  return max(words, key=len)


if __name__ == '__main__':
  main()