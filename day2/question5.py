# Given a list of names, concatenate them into a single string separated by spaces.

def main():
  names = ['John', 'Snow', 'Robb', 'Matt', 'Pet', 'Arya' ]
  print(joinWords(names))


def joinWords(data):
  return ' '.join(data)


if __name__ == '__main__':
  main()