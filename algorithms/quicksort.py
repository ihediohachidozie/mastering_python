# Quick sort
"""
Quick sort works by selecting one element (called “the pivot”) and finding the index 
where the pivot should end up in the sorted array.

The runtime of quicksort depends in part on how the pivot is selected. Ideally, it should 
be roughly the median value of the dataset being sorted.

The steps the algorithm takes are the following:

Identify the pivot value and place it in the index it should be.

Recursively execute the same process on each “half” of the data structure.

This algorithm has a O(n log n) complexity.
"""

arr = [3,2,1,4,6,5,7,9,8,10]

def swap(arr, idx1, idx2):
  arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
  return [arr[idx1], arr[idx2]]


def pivot(arr, start=0, end=len(arr)-1):
  pivot = arr[start]
  swap_idx = start

  i = start + 1
  while i <= end:
    if pivot > arr[i]:
      swap_idx += 1
      swap(arr, swap_idx, i)
    i += 1
  swap(arr, start, swap_idx)   

  return swap_idx


def quick_sork(arr, left=0, right=len(arr)-1):
  if left < right:
    pivot_index = pivot(arr, left, right)
    quick_sork(arr, left, pivot_index - 1)
    quick_sork(arr, pivot_index + 1, right)

  return arr

print(quick_sork(arr))








