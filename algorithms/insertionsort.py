"""
Insertion sort
Insertion sort orders the data structure by creating an “ordered half” that is always correctly sorted, and iterates through the data structure picking each value and inserting it in the ordered half exactly in the place it should be.
The steps it takes are the following:

It starts by picking the second element in the data structure.
It compares this element with the one before it and swap its positions if necessary.
It continues to the next element and if it’s not in the right position, it iterates through the “ordered half” to find its correct position and inserts it there.
It repeats the same process until the data structure is sorted.
This algorithm has a quadratic (O(n²)) complexity.

"""

arr = [3,2,1,4,6,5,7,9,8,10]

for x in range(len(arr)):
  current_val = arr[x]

  y = x - 1
  while y >= 0 and arr[y] > current_val:
    arr[y+1] = arr[y]
    y -= 1
  
  arr[y+1] = current_val


print(arr)

"""
The problem with bubble sort, selection sort, and insertion sort is that these algorithms don’t scale well.
There’re much better options we can choose when we’re working with big datasets. 
Some of them are merge sort, quick sort, and radix sort. So let's take a look at those now!
"""