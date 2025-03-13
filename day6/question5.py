"""Given a list of words, find the word with the maximum length and its length."""

def main():
  words = input('Enter the sentence: ').lower().split()
  print(f'The maximum word is "{maximum_word(words)[0]}" and length: {maximum_word(words)[1]}' )


def maximum_word(words):
  """Finds the longest word in a list words and it's length."""
  return max(words, key=len), len(max(words, key=len))


if __name__ == '__main__':
  main()