# import pyhon library to open webpages 
import webbrowser
# create class moveie
class Movie():

    # init function that create a new instance of class movie 
    def __init__(self,movie_title,movie_storyline,poster_image,trailer):
        self.title =movie_title
        self.storyline =movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer
        # function that opens the trailer video in the browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
