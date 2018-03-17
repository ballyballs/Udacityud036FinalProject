# Rays Favs

Rays Favs is an application that creates a webpage that displays movie tiles based on a user entered list of movies.

Each tile gives you the following:
1. Movie Image
      - clicking on the image will launch a youtube trailer
2. Movie Title
3. Movie Tagline
4. Movie Overview

The movie details are supplied via the movieDb api. The movieDb is a database of movies and tv programs

## PreRequisites

You need to install tmdbsimple. Installation and usage details [here](https://pypi.python.org/pypi/tmdbsimple)

One of the steps is to create register and get and API Key for the movieDB. Once you have you api key, locate the line:
_moviedb.API_KEY = '5c5354c3aa31e31a67ec9a4897882aee'_ and replace the key with the one you have created. Ensure you save the file afterwards.

## Usage
To create a website with your own list of favourite movies:
1. Ensure that you have [Python installed](https://www.python.org/downloads/)
2. Open the entertainment_center.py file
3. Locate the **movie_dict** and enter your "_Movie Name_" and its "_Release Date_" in double quotes, eg _movie_dict{"Star Wars":"1977"}_
## Running the program
1. Build the entertainment_center.py using python runtime of your choice.
