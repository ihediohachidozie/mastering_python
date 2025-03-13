"""Implement a function that removes a key-value pair from a dictionary."""

def main():
  person = {
    'name': 'John Doe',
    'age': 35,
    'address': '1055 Village Town',
    'status': 'Married'
  }

  print(person)
  remove_key_value(person, 'status')
  print(person)

def remove_key_value(my_dict, key):
  """Removes a key-value pair from a dictionary.

  Args:
      my_dict: The dictionary to modify.
      key: The key to remove.

  Returns:
      The modified dictionary.
  """
  if key in my_dict:
    del my_dict[key]
  return my_dict


if __name__ == '__main__':
  main()
