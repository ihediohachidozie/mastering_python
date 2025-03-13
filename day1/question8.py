'''Given a list of integers, find the sum of all positive numbers

'''

def main():
  myList = [1,2,3,-4]
  sumTotal = sum([x for x in myList if x > 0])
  print(f'The sum is {sumTotal}')

  # using in-built functions
  # filter() function in python is used to filter a sequence (like list, tuple or string)
  # base on a specific condition
  sum_total = sum(filter(is_positive, myList))
  print(f'Sum: {sum_total}')
 
def is_positive(x):
  if x > 0:
    return x
 
if __name__ == '__main__':
  main()