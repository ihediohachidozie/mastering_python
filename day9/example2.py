"""Create a class to represent a book with attributes like title, author, and publication year."""

class Book:
  def __init__(self, title, author, pub_year):
    self.title = title
    self.author = author
    self.pub_year = pub_year
  
  def __str__(self):
    return f"A book {self.title} by {self.author} published in {self.pub_year} "
  

book = Book('Handbook on Canvassing for the Consulship', 'Cicero', 1986)

print(book)

