"""Create a program that finds the common elements between two lists and stores them in a new list."""

def main():
  first_list = ['apple', 'orange', 'mango', 'kiwi', 'pineapple', 'carrot']
  second_list = ['carrot', 'apple', 'grape', 'kiwi']

  # professional method
  third_list = set(first_list).intersection(set(second_list))
  print(third_list)

  # naive method
  new_list = []
  copy_first = first_list.copy()
  copy_first.extend(second_list)

  for item in copy_first:
    if item in first_list and item in second_list:
      if item not in new_list:
        new_list.append(item)
  
  print(new_list)



if __name__ == '__main__':
  main()