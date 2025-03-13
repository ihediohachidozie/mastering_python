# Given a list of numbers, find the sum and average.

numbers = list(range(1,45,3))
print('Sum using in-built function')
print(f'Sum = {sum(numbers)}')
print(f'Average = {sum(numbers) / len(numbers)}')

# 2. Below code is when the size of the data is small. 
sum = 0
for x in numbers:
  sum += x

print('Sum using for loop')
print(f'Sum => {sum}')
print(f'Average => {sum / len(numbers)}')
