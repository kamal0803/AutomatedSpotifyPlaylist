import spotipy
import requests

class SpotifyPlaylistCreation:

    def __init__(self, client_ID, client_secret, redirect_uri, scope):
        self.client_ID = client_ID
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.scope = scope

    def get_access_token(self):

        sp = spotipy.oauth2.SpotifyOAuth(client_id=self.client_ID, client_secret=self.client_secret, redirect_uri=self.redirect_uri,scope=self.scope)
        access_token = sp.get_access_token(as_dict=False)

        return access_token

    def get_spotify_user_id(self, access_token):

        spotify_user_id_url = "https://api.spotify.com/v1/me"

        headers = {
            "Authorization": f"Bearer {access_token}"
        }

        spotify_user_id = (requests.get(spotify_user_id_url, headers=headers)).json()['id']

        return spotify_user_id

    def get_spotify_playlist_id(self, access_token, spotify_user_id, time_travel_date):

        new_playlist_url = f"https://api.spotify.com/v1/users/{spotify_user_id}/playlists"

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

        data = {
            "name": f"{time_travel_date} Billboard 100",
            "description": f"Playlist for the top 100 songs for the week of {time_travel_date}",
            "public": False
        }

        response = requests.post(new_playlist_url, headers=headers, json=data)

        spotify_playlist_id = response.json()['id']

        return spotify_playlist_id


    def get_songs_uri(self, top_100_songs, access_token, time_travel_date):

        top_100_songs_uri = []

        search_url_endpoint = "https://api.spotify.com/v1/search"

        headers = {
            "Authorization": f"Bearer {access_token}"
        }

        for song in top_100_songs:

            params = {
                "q": f'track:{song} year:{time_travel_date.split("-")[0]}',
                "type": "track"
            }

            try:
                response = requests.get(search_url_endpoint, params=params, headers=headers)
                top_100_songs_uri.append(response.json()["tracks"]["items"][0]["uri"])

            except:
                print(f"{song} doesn't exists in Spotify. Skipped.")

        return top_100_songs_uri


    def add_to_playlist(self, spotify_playlist_id, top_100_songs_uri, access_token):

        add_to_playlist_url = f"https://api.spotify.com/v1/playlists/{spotify_playlist_id}/tracks"

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

        for i in range(len(top_100_songs_uri)):

            data = {
                "uris": [
                    f"{top_100_songs_uri[i]}"
                ],
                "position": i
            }

            response = requests.post(add_to_playlist_url, headers=headers, json=data)

            print(response.json())
