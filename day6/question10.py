"""Implement a function that takes two lists and returns their union (all unique elelments from both lists)"""

def main():
  first_list = ['apple', 'orange', 'mango', 'kiwi', 'pineapple', 'carrot']
  second_list = ['carrot', 'apple', 'grape', 'kiwi']

  third_list = set(first_list).union(set(second_list))
  print(third_list)

  print(unique_elements(first_list, second_list))

def unique_elements(list_one, list_two):
  """Union of two lists.
  Args: 
    list_one: A list of values
    list_two: A list of values
  
  Returns:
    A list of unique elements from both lists.
  """
  list_one.extend(list_two)
  unique_list = []
  for ele in list_one:
    if ele not in unique_list:
      unique_list.append(ele)

  return unique_list

if __name__ == '__main__':
  main()