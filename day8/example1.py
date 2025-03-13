"""
Wrtie a program that reads a text file and prints its content.
"""

with open('data/demofile.txt', 'r') as reader:
  print(reader.read())


