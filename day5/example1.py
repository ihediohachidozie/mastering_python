"""Create a program that check if a given string is a palindrome."""
def main():
  userInput = input('Enter a text: ')
  if isPalindrome(userInput):
    print('It is a palindrome')
  else:
    print('It is not a palindrome')


def isPalindrome(words):
  left = 0
  right = len(words) - 1
  
  while left < right:
    if (words[left] != words[right]):
      return False
    left += 1
    right -= 1
    
    return True
  

if __name__ == '__main__':
  main()