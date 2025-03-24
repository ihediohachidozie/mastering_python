"""Create a class to represent a Movie with attributes like 
title, director, and rating"""

import sys

class Movie:
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = float(rating)


    
    def __str__(self):
        return f"\nTitle: {self.title}\nDirector: {self.director}\nRating: {self.rating}\n"
    
        

    @property
    def rating(self):
        return self._rating
    
    

    @rating.setter
    def rating(self, value):
        if 0 <= value <= 10:
            self._rating = value
        else:
            sys.exit("Rating must be between 0 and 10.")



def main():
    title = input("What's the title: ")
    director = input("What's the director: ")
    rating = float(input("What's the rating: "))

    movie = Movie(title, director, rating)

    print(movie)

    movie.rating = 11


if __name__ == "__main__":
    main()