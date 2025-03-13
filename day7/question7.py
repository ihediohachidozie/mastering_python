"""Given two sets, find the union, intersection, and difference between them."""


def main():
  fruit_basket_one = {'apple', 'banana', 'cherry'}
  fruit_basket_two = {'kiwi', 'orange', 'apple'}

  print(fruit_basket_one | fruit_basket_two)
  print(fruit_basket_one & fruit_basket_two)
  print(fruit_basket_one - fruit_basket_two)


if __name__ == '__main__':
  main()