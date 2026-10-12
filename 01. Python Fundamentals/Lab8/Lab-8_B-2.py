# Lab-8_B-2

# Represent the same information using a Movie class.

class Movie:
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating
    
movie = Movie("Persona", "Ingmar Bergman", 10)

print(movie.title, movie.director, movie.rating)