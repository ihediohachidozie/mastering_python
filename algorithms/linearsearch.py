# Linear Search
# Linear search consists of iterating over the data structure one 
# value at a time and checking if that value is the one we’re looking for. 
# It’s probably the most intuitive kind of search and the best we can do if 
# the data structure we’re using isn’t ordered.

"""Let’s say we have an array of numbers and for this array we want to write 
a function that takes a number as the input and returns that number’s index 
in the array. In case it doesn’t exist in the array, it will return -1. 
A possible approach could be the following:
"""

arr = [1,2,3,4,5,6,7,8,9,10]

def linear_search(arr, num):
  for x, ele in enumerate(arr):
    if num == ele:
      return x
  return -1

print(linear_search(arr, 5))
print(linear_search(arr, 11))

"""As the array isn’t ordered, we don’t have a way of knowing the approximate 
position of each value, so the best we can do is check one value at a time. 
The complexity of this algorithm is linear - O(n) since in the worst case scenario 
we will have to iterate over the whole array once to get the value we’re looking for.""" 