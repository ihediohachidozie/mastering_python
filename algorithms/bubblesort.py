"""Bubble sort
Bubble sort iterates through the data structure and compares one pair of values at a time. If the order of those values is incorrect, it swaps its positions to correct it. The iteration is repeated until the data is ordered. This algorithm makes bigger values “bubble” up to the end of the array.

This algorithm has a quadratic – O(n²) complexity since it will compare each value with the rest of the values one time."""
import random

arr = [3,2,1,4,6,5,7,9,8,10]

def bubble_sort(arr):
  for x in range(len(arr)):
    for y in range(x+1, len(arr)):
      if arr[x] > arr[y]:
        arr[x], arr[y] = arr[y], arr[x]
  return arr
  
print(bubble_sort(arr))