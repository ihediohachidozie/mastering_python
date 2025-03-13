"""Create a function that takes a list of sentences and writes them to a new text file, each on a line."""
import sys

def main():
  sentences = """Hugh went to the shop.
  Terry was late for the bus.
  The car ran a red light.
  Liam took out the bins.
  I drink coffee every morning.
  There's one cookie left.
  He has a pet chinchilla.
  The train leaves every morning at 18 AM""".split('.')
  
  #sentences = [sentence.replace('\n', '') for sentence in sentences]
  copy_file(sentences)



def copy_file(sentences):
  """Copy list of sentences to a file.
  Arg:
    sentence: A list of sentences 
  Returns:
    A confirmation for a new file creation with the 
    list of sentences as content.
  """
  with open('data/demo1.txt', 'w') as writer:
    for line in sentences:
      writer.write(line)
  
  print('File copying completed')



if __name__ == '__main__':
  main()