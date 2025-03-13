# Merge Sort

# Merge sort is an algorithm that recursively decomposes the data structure into individual values, 
# and then composes it again in a sorted way.

# The steps it takes are the following:

# Recursively break up the data structure into halves until each “piece” has only one value.

# Then, recursively merge the pieces in a sorted way until it gets back to the length of the original 
# data structure.

# This algorithm has a O(n log n) complexity, since the decomposition part of it has a complexity of 
# log n and the comparison part of it has a complexity of n.

arr = [3,2,1,4,6,5,7,9,8,10]

# Merge function
def merge(arr1, arr2):
  result = []
  i = 0
  j = 0

  while i < len(arr1) and j < len(arr2):
    if arr2[j] > arr1[i]:
      result.append(arr1[i])
      i += 1
    else:
      result.append(arr2[j])
      j += 1
  
  while i < len(arr1):
    result.append(arr1[i])
    i += 1
  
  while j < len(arr2):
    result.append(arr2[j])
    j += 1
  
  return result


def merge_sort(arr):
  if len(arr) <= 1:
    return arr
  
  mid = len(arr)//2
  left = merge_sort(arr[:mid])
  right = merge_sort(arr[mid:])

  return merge(left, right)


print(merge_sort(arr))



