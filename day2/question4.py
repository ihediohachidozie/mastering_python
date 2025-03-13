#Create a function to reverse a given string.
def main():
  text = input('Enter any text of your choice: ').strip()
  textReverse(text)
  print(reverse_string(text))
  
  # reversing an int value
  num = 8851
  print(int(str(num)[::-1]))


def textReverse(data):
  x = len(data) - 1
  print()
  while x >= 0:
    print(data[x], end='')
    x -= 1

def reverse_string(text):
  return text[::-1]

if __name__ == "__main__":
  main()
