class Employee:
  def __init__(self, name, age, position, year):
    self.name = name
    self.age = age
    self.position = position
    self.year = year

  def __str__(self):
    return f'{self.name} is {self.age}, {self.position} employed in {self.year}.'

employees = [
  {'chuka': ['Chuka', 41, 'IT Officer', 2009]},
  {'kirk': ['James Kirk', 34, 'Captain', 2265]},
  {'spock': ['Spock', 35, 'Science Officer', 2254]},
  {'mccoy': ['Leonard McCoy', 26, 'Chief Medical Officer', 2266]}
]

# for employee in employees:
#   for key, value in employee.items():
#     #print(key, value)
#     key = Employee(*value)
#     print(key.name)

chuka = ['Chuka', 41, 'IT Officer', 2009]
kirk = ['James Kirk', 34, 'Captain', 2265]
spock = ['Spock', 35, 'Science Officer', 2254]
mccoy = ['Leonard McCoy', 26, 'Chief Medical Officer', 2266]

chuka = Employee(*chuka)
kirk = Employee(*kirk)
spock = Employee(*spock)
mccoy = Employee(*mccoy)

print(chuka)
print(kirk)
print(spock)
print(mccoy)
