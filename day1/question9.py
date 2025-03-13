"""Create a program that takes a sentence as input and 

counts the number of words in it.
"""

def main():
  sentence = input("Enter a sentence: ")
  print(len(sentence.split()))

  # print(len(input("Enter a sentence: ").split()))

if __name__ == '__main__':
  main()