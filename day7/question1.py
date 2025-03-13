"""Given two dictionaries, merge them into a single dictionary."""

dict_one = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1984
}

dict_two = {
  'color': 'red'
}

dict_one.update(dict_two)
print(dict_one)