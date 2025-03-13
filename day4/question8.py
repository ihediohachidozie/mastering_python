"""Wrtie a function that takes two lists and returns their intersection (common elements)."""

def main():
  myList1 = [1,2,3,4]
  myList2 = [1,5,6,3]
  print(listIntersection(myList1, myList2)) # not efficient

  print(list(set(myList1).intersection(set(myList2))))


def listIntersection(list1, list2):
  return [x for x in list1 if x in list2]


if __name__ == '__main__':
  main()