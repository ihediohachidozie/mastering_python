"""Calculate the sum of digits of a given number."""
number = 1234

# method 1
print(sum([int(x) for x in str(number)]))

# method 2
sum = 0
for x in str(number):
  sum += int(x)
print(sum)

