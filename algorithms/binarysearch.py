# Binary Search approach
# When we have an ordered data structure, there’s a much more efficient 
# approach we can take, binary search. What we do in binary search is the following:

# Select the middle value of our data structure and “ask”, is this the value we’re looking for?

# If not, we “ask” whether the value we’re looking for is greater or less than the middle value?

# If it’s greater, we “discard” all the values smaller than the mid value. If it’s smaller, 
# we “discard” all the values greater than the mid value.

# And then we repeat the same operation until we find the given value or the remaining 
# "piece" of the data structure can't be divided anymore.

"""Write a program that takes a number and a list as the input and returns the number's index in the array.
In case it doesn't exist in the array, it will return -1. Let's say we have an ordered list"""
 
arr = [1,2,3,4,5,6,7,8,9,10]
num = 5
def search(arr, num):
  # We will use three pointers.
  # One at the start of the list, one at the end and another at the middle.
  start = 0
  end = len(arr) - 1
  middle = (start + end) // 2

  # While we haven't found the number and the start pointer is equal or smaller to the end pointer
  while arr[middle] != num and start <= end:
    #print(f'Middle num => {middle}')
    # if the desired number is smaller than the middle, discard the bigger half of the array
    if num < arr[middle]:
      end = middle - 1
      # if the desired number is bigger than the middle, discard the smaller half of the array
    else:
      start = middle + 1
    # Recalculate the middle value
    middle = (start + end) // 2
  # if we've exited the loop it means we've either found the value or the array can't be divided further
  return middle if arr[middle] == num else -1

num = 8
print(f'The value {num} is at index number {search(arr, num)}')

# This approach may seem like “more code” at first, but potential iterations are actually a 
# lot less than in linear search, and that’s because in each iteration we’re discarding roughly 
# half of the data structure. The complexity of this algorithm is logarithmic – O(log n).



