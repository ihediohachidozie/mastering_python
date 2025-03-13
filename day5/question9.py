"""Write a function to remove all duplicate characters from a given string."""

def main():
  userInput = input('Enter the string: ')
  print(removeDuplicates(userInput))


def removeDuplicates(myString):
  myList = [myString[x] for x in range(len(myString))]
  myList = list(dict.fromkeys(myList))
  return ''.join(myList)



if __name__ == '__main__':
  main()