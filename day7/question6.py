"""Write a Python program that counts the number of occurrences of each character in a given string using a dictionary."""
from collections import Counter

def main():
  word_dict = {}
  my_string = '''Write a Python program that counts the number of occurrences of 
                each character in a given string using a dictionary'''
  
  words = my_string.lower().split()

  word_dictionary = Counter(words)
  print(word_dictionary)
  print(word_dictionary.most_common(1)) # highest occurrence

  for word in words:
    if word not in word_dict.keys():
      word_dict[word] = 1
    else:
      word_dict[word] += 1

  print(word_dict)
  

if __name__ == '__main__':
  main()