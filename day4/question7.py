"""Create a function that takes a list of strings and returns the list sorted alphabetically."""

def main():
  text = 'hello world'
  print(sortedStrings(text))


def sortedStrings(text):
  myList = [text[x] for x in range(len(text)) if text[x] != ' ']
  myList.sort()
  return myList

  for x in range(len(myList)):
    for y in range(x+1, len(myList)):
      if myList[x] > myList[y]:
          myList[x], myList[y] = myList[y], myList[x]
  return myList


if __name__ == '__main__':
  main()