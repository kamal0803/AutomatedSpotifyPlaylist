from billboard_webpage_scrapping import BillBoardScrapping
from spotify_py import SpotifyPlaylistCreation

time_travel_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

URL = f"https://www.billboard.com/charts/hot-100/{time_travel_date}/"

client_ID = YOUR_CLIENT_ID
client_secret = YOUR_CLIENT_SECRET
redirect_uri = "https://example.com/"
scope = "playlist-modify-private"

bill_board_scrapping = BillBoardScrapping(URL)
top_100_songs = bill_board_scrapping.top_100_songs_of_the_week()

spotify_playlist_creation = SpotifyPlaylistCreation(client_ID, client_secret, redirect_uri, scope)

access_token = spotify_playlist_creation.get_access_token()
spotify_user_id = spotify_playlist_creation.get_spotify_user_id(access_token)
spotify_playlist_id = spotify_playlist_creation.get_spotify_playlist_id(access_token, spotify_user_id, time_travel_date)
songs_uri = spotify_playlist_creation.get_songs_uri(top_100_songs, access_token, time_travel_date)
final_playlist = spotify_playlist_creation.add_to_playlist(spotify_playlist_id, songs_uri, access_token)
