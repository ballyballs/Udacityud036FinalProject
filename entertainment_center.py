import media
import fresh_tomatoes
import movie_details
"""
entertainment center file

This file is where the user adds their key/value pair of Movie and release date.
This is then supplied to the moviedb to find out the images/trailers and movie details
"""
#lists defined to be used later
movies=[]
fav_movies=[]
"""
movie dict dictionary.

This dictionary is where the user enters a key/value pair of the movie name and its release date
"""

movie_dict={"Up":"2009",  "Wall-E":"2008", "Demolition Man": "1993", "Empire Strikes Back":"1980", "Return Of The Jedi": "1983", "Black Panther": "2018"}
#for loop that uses the movie_dict to create a list that is used to hold the result of calling the moviedb for each movie
for x in movie_dict.items():
    movie=x[0]
    date=x[1]
    fav_movie=movie_details.Movie_Details(x[0],x[1])
    fav_movies.append(fav_movie)
# Pass each movie with its details to the fresh_tomatoes file to display on the webpage
for movie in fav_movies:
    movie_details=media.Movie(movie.movie_title, movie.movie_info_details()['tagline'],movie.movie_info_details()['overview'], movie.movie_poster_details(), movie.movie_trailer_details())
    movies.append(movie_details)
fresh_tomatoes.open_movies_page(movies)

