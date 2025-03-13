"""Create a loop that prints the first 10 even numbers."""

"""
# Method 1 
counter = 0
for x in range(100):
  if x > 0 and x % 2 == 0:
    print(f'{x} is an even number')
    counter += 1
  if counter == 10:
    break 
"""

number, counter = 0, 0
while counter <= 10:
  if number > 0 and number % 2 == 0:
    print(f'{number} is an even number')
    counter += 1
  number += 1
  
def is_even(number):
  if number > 0 and number % 2 == 0:
    return number


print(list(filter(is_even, range(21))))
