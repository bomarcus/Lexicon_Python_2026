# Lab-8_C-1

# Add a method to Movie that returns whether the movie is highly rated.
# Choose a sensible rating threshold.

class Movie:
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating

    def rating_eval(self):
        if self.rating > 5:
            return "Pretty good!"
        else:
            return "pretty bad!"


movie = Movie("Persona", "Ingmar Bergman", 10, )

print(movie.title, movie.director, movie.rating, movie.rating_eval())
