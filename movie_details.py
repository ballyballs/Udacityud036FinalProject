
import tmdbsimple as moviedb


class Movie_Details():
    """
    movie details docs.

    the Movie_Details class sets up a connection to the movieDb.
    It searches for the movie using the title and release date passed into
    the constructor
    it contains methods to:
    1) find and return the poster image
    2) find and return the trailer address on youtube
    3) find and return the tagline and overview
    """

    def __init__(self, movie_title, movie_release_date):
        """ Initialises the Movie_Details Class.

        uses the tmdbsimple library to connect to the moviedb api
        uses a key to securely connect
        sets up the connection and sets some object level
        variables to be used in the methods
        """
        self.movie_title = movie_title
        self.movie_release_date = movie_release_date
        # setup the apikey required to connect to the moviedb
        moviedb.API_KEY = '5c5354c3aa31e31a67ec9a4897882aee'
        self.config = moviedb.Configuration()
        # search for the movie in the moviedb
        self.moviedb_search = moviedb.Search()
        response = self.moviedb_search.movie(
            query=movie_title, year=movie_release_date)

    def movie_poster_details(self):
        """ This returns the url for the films poster on movieDB.

        assumes that only 1 movie has the name and release date in the db
        it takes the self object as a paramater

        sets a default poster size to fit the screen

        returns poster_url
        """
        # default poster size
        poster_size = 'w154'
        # default image path of the moviedb
        poster_path = self.config.info()['images']['secure_base_url']
        # poster location
        poster = self.moviedb_search.results[0]['poster_path']
        poster_url = poster_path + poster_size + poster
        return poster_url

    def movie_trailer_details(self):
        """ This returns a youtube video id for the films trailer.

        assumes that only 1 movie has the name and release date in the db
        it takes the self object as a paramater

        returns trailer_key
        """
        # find the movie id from the moviedb search
        movie_id = self.moviedb_search.results[0]['id']
        # Movies class returns different data to generic moviedb movie search
        movie = moviedb.Movies(movie_id)
        trailer = movie.videos()['results'][0]
        trailer_key = trailer['key']
        return trailer_key

    def movie_info_details(self):
        """ This returns the movie tagline and movie overview.

        assumes that only 1 movie has the name and release date in the db
        it takes the self object as a paramater

        returns movie_info dict with the tagline and overview as keys
        """
        movie_id = self.moviedb_search.results[0]['id']
        movie = moviedb.Movies(movie_id)
        tagline = movie.info()['tagline']
        overview = movie.info()['overview']
        movie_info = {'tagline': tagline, 'overview': overview}
        return movie_info
