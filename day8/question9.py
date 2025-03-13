"""Write a function that reads a JSON file and extracts specific information from it."""
import pandas as pd
import json

def main():
  file_path = 'data/sample4.json'
  age_limit = 25
  read_json(file_path, age_limit)

def read_json(file_path, age_limit):
  """
  Reads a JSON file and extracts specific information.
  Args:
      file_path: Path to the JSON file.
      age_limit: criteria for extracting the information.
  
  Returns:
    A dictionary containing the extracted information.
  """
  # Method 1:
  
  data = pd.read_json(file_path)

  for people in data['people']:
    if people['age'] < age_limit:
      print(people)

  # Method 2:

  # with open('data/sample4.json', 'r') as file:
  #   persons = json.load(file)
  
  # for person in persons['people']:
  #   if person['age'] > 25 :
  #     print(person)

if __name__ == '__main__':
  main()