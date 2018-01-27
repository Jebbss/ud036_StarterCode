import webbrowser
class Movie():
    def __init__(self, movie_title, movie_summary, movie_trailer, movie_poster):
        self.title = movie_title
        self.summary = movie_summary
        self.trailer_youtube_url = movie_trailer
        self.poster_image_url = movie_poster

    def show_trailer(self):
        webbrowser.open(self.trailer)
