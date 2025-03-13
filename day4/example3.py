#Implement a function that reverses a given string.
def main():
  userInput = input('Enter any text of your choice: ').strip()

  reverseText(userInput)

  print(reverse_string(userInput)) # better version


def reverse_string(words):
  return words[::-1]

def reverseText(words):
  x = len(words) - 1
  print()
  while x >= 0:
    print(words[x], end=' ')
    x -= 1
  

if __name__ == "__main__":
  main()
