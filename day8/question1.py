"""Write a Python program to copy the contents of one text file into another."""
import sys

def main():
  source = 'demofile.txt'
  destination = 'demo.txt'
  copy_files(source, destination)


def copy_files(source, destination='example.txt'):
  """Copy the content of a text file to another.
  
  Args:
    source: The file content to be copied from.
    destination: The file to be copied to.
        
  Returns:
    A confirmation message: files copied successfully.
  """
  try:
      with open(f'data/{source}', 'r') as reader:
        text_to_write = reader.readlines()

      with open(f'data\{destination}', 'w') as writer:

        for text in text_to_write:
          writer.write(text)

      print('File copied successfully.')
  except:
    sys.exit('Something went wrong. File copying unsuccessful')

if __name__ == '__main__':
  main()