"""
Create a new text file and write some content into it.
"""

with open('data/demofile.txt', 'r') as reader:
  text_to_write = reader.readlines()


with open('data\demo.txt', 'w') as writer:
  for text in text_to_write:
    writer.write(text)