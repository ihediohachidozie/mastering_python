"""Create a function that takes a list of strings and returns 
the list sorted by the length of the strings"""

def main():
  my_string = "This is a test string from Andrew".split()
  print(sorted_list(my_string))

  print(sort_strings(my_string))


def sorted_list(my_string):
  """Sort list of strings by their length
  Args:
    words: A list of words.

  Returns:
    A list of sorted words by their length.
  """
  return sorted(my_string, key=len)


def sort_strings(words):
  """Sort list of strings by their length
  Args:
    words: A list of words.

  Returns:
    A list of sorted words by their length.
  """

  if not words:
    return None
  
  for x in range(len(words)):
    for y in range((x+1), len(words)):
      if len(words[x]) > len(words[y]):
        words[x], words[y] = words[y], words[x]
  
  return words

if __name__ == '__main__':
  main()