import webbrowser


class Movie():
    """Class to store information about a movie for entertainment center"""
    def __init__(self, movie_title, movie_summary, movie_trailer,
                 movie_poster):
        self.title = movie_title
        self.summary = movie_summary
        self.trailer_youtube_url = movie_trailer
        self.poster_image_url = movie_poster

    # Opens a a movie trailer in a web browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
