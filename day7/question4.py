"""Create a program that checks if two sets have any elements in common."""

def main():
  fruit_basket_one = {'apple', 'banana', 'cherry'}
  fruit_basket_two = {'kiwi', 'orange', 'apple'}

  fruit_basket_three = fruit_basket_one & fruit_basket_two

  print(fruit_basket_three)





if __name__ == '__main__':
  main()