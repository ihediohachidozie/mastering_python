"""Write a program that takes a sentence as input and counts the number of words in it."""

def main():
  userInput = input('Enter a sentence: ')
  print(countWords(userInput))


def countWords(words):
  return len(words.split(' '))


if __name__ == '__main__':
  main()





