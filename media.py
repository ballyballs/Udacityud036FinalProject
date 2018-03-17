class Movie():
    """
    Movie docs.

    the Movie class has 1 method, which is the overridden init method.
    When this is called it sets the
    1) title
    2) poster url
    3) youtube video id
    4) movie tagline
    5) movie overview
    """

    def __init__(self, title, tag_line, overview, poster_url,
                 youtube_video_id):
        self.title = title
        self.poster_url = poster_url
        self.youtube_video_id = youtube_video_id
        self.tag_line = tag_line
        self.overview = overview
