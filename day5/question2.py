"""Create a function to reverse a given string."""

def main():
  userInput = input('Enter the string: ')
  print(reversedText(userInput))
  print(reverse_string(userInput))


def reverse_string(words):
  return words[::-1]

def reversedText(words):
  counter = len(words) - 1 
  newText = ''
  while counter >= 0:
    newText += words[counter]
    counter -= 1
  return newText


if __name__ == '__main__':
  main()