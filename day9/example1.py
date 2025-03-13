"""Create a class to represent a basic calculator with add, subtract, multiply and divide methods."""
import sys
class Calculator:

  def __init__(self, number1, number2):
    self.number1 = number1
    self.number2 = number2

  def __str__(self):
    return 'This is a calculator app'

  def add(self):
    return self.number1 + self.number2
  

  def subtract(self):
    return self.number1 - self.number2
  

  def multiply(self):
    return self.number1 * self.number2
  

  def divide(self):
    try:
      return self.number1 / self.number2
    except ZeroDivisionError:
      sys.exit('Division by zero')

math_work = Calculator(0,4)
print(math_work)
print(math_work.add())
print(math_work.subtract())
print(math_work.multiply())
print(math_work.divide())