# Given a list of numbers, find the maximum and minimum values.

def main():
  myList = [2,3,100,8,-2,-5,99,40,0,999]
  print(f'Maximum value = {max(myList)}')
  print(f'Minimum value = {min(myList)}')

  # alternative when the size of the data sample is small.
  maximumValue, minimumValue = getMaximumAndMinimumValues(myList) 

def getMaximumAndMinimumValues(myList):
  for x in myList:
    maxValue = x
    minValue = x
    for i in myList:
      if maxValue < i:
        maxValue = i # maximum value
      elif minValue > i:
        minValue = i # minimum value
  return maxValue, minValue


if __name__ == '__main__':
  main()