"""Implement a function that takes a list of strings and returns a set of unique characters present in all strings."""
def main():
  my_string = """Implement a function that takes a list of strings and 
  returns a set of unique characters present in all strings."""
  words = my_string.lower().split()

  print(unique_characters(words))


def unique_characters(words):
  """Get unique characters from a list of strings.
  Args:
    words: A list of strings.
  
  Returns:
    A list of unique characters.
  """
    
  #unique_char = set()
  characters = [word[x] for word in words for x in range(len(word)) if word[x] not in ['.']]
  unique_characters = list(dict.fromkeys(characters))

  return unique_characters

  for word in words:
    for x in range(len(word)):
      if word[x] not in ['.', '?', '!', '-', '_', '(', ')']:
        unique_char.add(word[x])
  
  return list(unique_char)

if __name__ == '__main__':
  main()