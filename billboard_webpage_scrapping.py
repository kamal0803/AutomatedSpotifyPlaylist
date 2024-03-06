import requests
from bs4 import BeautifulSoup

class BillBoardScrapping:

    def __init__(self, URL):
        self.URL = URL

    def top_100_songs_of_the_week(self):

        response = requests.get(self.URL)
        billboard_web_page = response.text

        soup = BeautifulSoup(billboard_web_page, "html.parser")

        songs = soup.select(selector="#title-of-a-story")
        song_class_ = "c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only"

        top_100_songs = []

        for song in songs:
            if song_class_ in str(song):
                top_100_songs.append(song.getText().strip())

        return top_100_songs

