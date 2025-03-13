"""Given a list of words, count the number of words with more than five characters."""

myList = 'Given a list of words count the number of words with more than five characters'.split()

# method 1.

def is_above_five_characters(word):
  if len(word) > 5:
    return word
  
print(len(list((filter(is_above_five_characters, myList)))))

# method 2
print(len([x for x in myList if len(x) > 5]))

# method 3
counter = 0
for x in myList:
  if len(x) > 5:
    counter  += 1
print(counter)
