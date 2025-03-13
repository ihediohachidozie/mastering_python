"""
Selection sort
Selection sort is similar to bubble sort but instead of placing the bigger 
values at the end of the data structure, it focuses on placing the smaller 
values at the beginning. The steps it takes are the following:

Store the first item of the data structure as the minimum value.

Iterate through the data structure comparing each value with the minimum value. 
If a smaller value is found, it identifies this value as the new minimum value.

If the minimum value isn’t the first value of the data structure, it swaps the 
positions of the minimum value and the first value.

It repeats this iteration until the data structure is ordered.

This algorithm has a quadratic – O(n²) complexity.
"""

arr = [3,2,1,4,6,5,7,9,8,10]

for x in range(len(arr)):
  for y in range(x+1, len(arr)):
    if arr[y] < arr[x]:
      arr[x], arr[y] = arr[y], arr[x]


print(arr)
