import pprint
import spotipy
import requests
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
client_id = "254310f18aac4cbbb36c393f6787fade"
token = "BQClIduc0GPvHuQTR_Lk6W_XoxWKBksHaovMxE5A6jBHp7cRgmIRy4O-4jvrjRv-7aBFIqzFdbjDgSrFyrfh7h1pU6pxaaKnxTOJ5u6BN4ismNqwLoKhrWId0YChG6R4Quy5vjzueMNeedp9W22n5e0MRlrM5oAQ5JywzAPM8LmbObWX-r-qFoRKmfJl049K7jXyvGVENejecJUSvK-iz8DPbV870Fcl5eHoEHCX8xJgIpVCRbxYFimUjVGR_hQ9-U5tZRlk-r2LgmLjhuBnJ8KkbtO0gw"
client_secret = "fdbc6e73c81941a4ac739f3d0a410902"
user_id = "31hkm5aiwww3cy6bw4k5hnuznvba"
redirect_uri = "http://localhost:8888/callback"

chosen_year = input("Which year do you want to travel to? Type the date in this format YYYY: ")

response = requests.get(f"https://www.billboard.com/charts/year-end/{chosen_year}/hot-100-songs/")
contents = response.text

soup = BeautifulSoup(contents, 'html.parser')
top100_tag = soup.find_all(name='h3', class_="a-font-primary-bold-s")
top100_artisttag = soup.find_all(name='span', class_='a-font-primary-s')
top100_track = [music.get_text().strip() for music in top100_tag]
top100_artist = [artist.get_text().strip() for artist in top100_artisttag]


scope = "user-library-read playlist-modify-private playlist-modify-public"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id,client_secret=client_secret,redirect_uri=redirect_uri))
results = sp.current_user_saved_tracks()
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
token_info = auth_manager.cache_handler.get_cached_token()
sp = spotipy.Spotify(auth_manager=auth_manager)

sp.user_playlist_create(user=user_id, name=chosen_year)
last_playlist_id = sp.user_playlists(user=user_id)['items'][0]['id']

contador = 0
old_music_uri = []

for music in top100_track:

    artist = top100_artist[contador]
    search_string = f"track:{music}  artist:{artist}"
    search = sp.search(q=search_string, limit=1, type='track')
    for item in search['tracks']['items']:
        music_uri = [item['uri']]

    print(f"{music_uri}/{old_music_uri} {music}/{artist}")

    if music_uri not in old_music_uri:
        sp.playlist_add_items(playlist_id=last_playlist_id, items=music_uri)
        old_music_uri.append(music_uri)
    contador += 1




