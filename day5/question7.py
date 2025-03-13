"""Create a function that takes a sentence as input and returns the sentence in reverse order."""

def main():
  userInput = input('Enter the string: ')
  print(reversedText(userInput))

  print(reverse_string(userInput))

def reverse_string(words):
  return words[::-1]

def reversedText(sentence):
  """Return sentence in reverse order"""
  counter = len(sentence) - 1 
  newSentence = ''
  while counter >= 0:
    newSentence += sentence[counter]
    counter -= 1
  return newSentence


if __name__ == '__main__':
  main()