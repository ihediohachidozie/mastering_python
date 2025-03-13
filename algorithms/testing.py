# Write a function that takes two parameters: A non-empty array of distinct integers and an integer representing
# a target sum. If any two numbes in the array sum up to the target sum, the function should return them in an 
# array. If no two numbers sum up to the target sum, the function should rtrun an empty array.

def main():
  integerArray = [9,1,3,4,5]
  targetSum = 6
  print(two_number_sum1([9,1,3,4,5], 6))
  print(two_number_sum1([1,2,3,4,5], 10))
  
  print(two_num_sum([9,1,3,4,5], 6))
  print(two_num_sum([1,2,3,4,5], 10))

  print(two_num_sum1([9,1,3,4,5], 6))
  print(two_num_sum1([1,2,3,4,5], 7))


def two_number_sum1(integerArray, targetSum):
  for x in range(len(integerArray)):
    for y in range(x+1, len(integerArray)):
      if targetSum == integerArray[x] + integerArray[y]:
        return [integerArray[x], integerArray[y]]
  return []    


def two_num_sum(array, target):
  array.sort()

  left = 0
  right = len(array) - 1

  while left < right:
    current_sum = array[left] + array[right]
    if current_sum == target:
      return [array[left], array[right]]
    else:
      if current_sum < target:
        left += 1
      else:
        right -= 1
      

  
  return []


def two_num_sum1(array, target):
  """Beta method"""
  result = []

  for x in range(len(array)):
    number = target - array[x]
    try:
      if array.index(number) in array and array.index(number) != x:
        print(array[x])
        print(array[array.index(number)])
        result.append(array[x])
        result.append(array[array.index(number)])
        break
    except:
      pass
  
  return result


if __name__ == '__main__':
  main()