"""Write a program that converts a given number of days 
into years, weeks, and days.
"""

numberOfDay = int(input("Enter the number of days: "))

year = numberOfDay / 365
week = numberOfDay / 7
month = numberOfDay / 30

print(f'Years: {year}')
print(f'Month: {month}')
print(f'Week: {week}')