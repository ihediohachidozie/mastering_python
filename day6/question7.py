"""Given a list of names, remove all duplicate names and print the unique names."""

def main():
  names = ['olivia', 'noah', 'amelia', 'liam', 'emma', 'oliver', 'sophia', 'elijah', 'noah', 'emma', 'olivia', 'liam']

  unique_names = list(set(names))

  print(unique_names)

  print(remove_duplicates(names))

def remove_duplicates(names):
  """Remove duplicate names in a list.
  Args:
    names: A list of names.

  Returns:
    A list of unique names.
  """
  unique_names = []
  for name in names:
    if name not in unique_names:
      unique_names.append(name)

  return unique_names

if __name__ == '__main__':
  main()