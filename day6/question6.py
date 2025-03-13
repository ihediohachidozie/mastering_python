""" Write a Python program to count the occurrences of each 
element in a given list"""

from collections import Counter

def main():
  my_list = ['Apple', 'Orange', 'Cherry', 'Apple', 'Mango', 'Pineapple', 'Kiwi']
  print('Item', 'Count'.rjust(20))
  count_elements(my_list)

  print(count_element(my_list)) # using dictionary

  print(Counter(my_list)) # using in-built function

  
def count_elements(my_list):
  """Count the occurrences of each element in a given list.
  Args:
    my_list: A list of elements with duplicates.
  
  Returns:
    Print each element and number of occurrences.
  """
  unique_elements = []
  for ele in my_list:
    if ele not in unique_elements:
      unique_elements.append(ele)

  
  for ele in unique_elements:
    count = my_list.count(ele)
    print (f'{ele:10} : {count:10}')


def count_element(my_list):
  """Count the occurrences of each element in a given list.
  Args:
    my_list: A list of elements with duplicates.
  
  Returns:
    A dictionary with each element as key and number of occurrences as value.
  """
  unique_elements = {}
  for ele in my_list:
    if unique_elements.get(ele):
      unique_elements[ele] += 1
    else:
      unique_elements.update({ele: 1})
  
  return unique_elements

if __name__ == '__main__':
  main()