# Create a Python function to check if a given string is a palindrome

def main():
  userInput = input('Enter a text: ')
  if is_palindrome(userInput):
    print('It is a palindrome')
  else:
    print('Not a palindrome')


def is_palindrome(word):
  left = 0
  right = len(word) - 1
  while (left < right):
    if word[left] != word[right]:
      return False
    left += 1
    right -= 1
  return True


if __name__ == '__main__':
  main()