"""Given a text file with a list of numbers, wrtie a function that finds the sum of all numbers in the file."""

sum = 0

with open('data/numbers.txt', 'r') as reader:
  numbers = reader.read()
  for number in numbers.split():
    sum += int(number)



print(f"The total sum of numbers is = {sum}")