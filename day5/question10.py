"""Implement a program that takes a sentence and a word as input and checks if the word is present in the sentence."""

def main():
  sentence = 'Implement a program that takes a sentence and a word as input and checks if the word is present in the sentence'
  word = 'program'
  print(isPresent(sentence, word))


def isPresent(sentence, word):
  splitSentence = sentence.split()
  return True if word in set(splitSentence) else False



if __name__ == '__main__':
  main()