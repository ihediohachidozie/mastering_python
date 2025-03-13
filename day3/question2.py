"""Given a list of integers, find all the even numbers and store them in a new list."""


myList = [2,4,3,7,8,9,11,13,14,17,20,30]

# method 1

isEven = [x for x in myList if x % 2 == 0]
print(isEven)

# method 2
def is_even(x):
  if x % 2 == 0:
    return x

even_numbers = list(filter(is_even, myList))


print(even_numbers)


