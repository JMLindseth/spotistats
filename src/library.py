import os
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials
import matplotlib.pyplot as plt

load_dotenv()

SPOTIPY_CLIENT_ID = os.getEnv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getEnv('SPOTIPY_CLIENT_SECRET')

auth_manager = SpotifyClientCredentials(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET
)
sp = spotipy.Spotify(auth_manager=auth_manager)




def printPlaylists(username):
    playlists = sp.user_playlists(username)
    while playlists:
        for i, playlist in enumerate(playlists['items']):
            print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None


def printArtis(artistid):
    info = sp.artist(artistid)
    print(info)


def artist_in_playlist(songs):
    artist_dict = {}

    for i, song in enumerate(songs['tracks']['items']):
        track = song['track']
        artist_name = track['artists'][0]['name']
        if artist_name in artist_dict:
            artist_dict[artist_name] += 1
        else:
            artist_dict[artist_name] = 1

    # print(artist_dict)
    # print(len(artist_dict.items()))

    return artist_dict

def dict_with_values_above_x(dict, x):
    filtered = {key: value for (key, value) in dict.items() if value > x}
    return filtered

def artist_bar_graph(artists):
    fig = plt.figure()
    ax = fig.add_subplot(211)
    artist_names = artists.keys()
    num_songs = artists.values()
    ax.bar(artist_names, num_songs)
    plt.xticks(rotation=90)
    plt.show()


def printPlaylist(playlistId):
    songs = sp.playlist(playlistId)
    # print(songs)

    # print(songs['tracks']['items'][0]['track']['name'])
    # print(songs['tracks']['items'][0]['track']['artists'][0]['name'])


    for i, song in enumerate(songs['tracks']['items']):
        track = song['track']
        track_name = track['name']
        artist_name = track['artists'][0]['name']
        # print("Name: %s, artist: %s" % (track_name, artist_name))

    artist_dict = artist_in_playlist(songs)
    sorted_artist_dict = dict(sorted(artist_dict.items(), key=lambda item: item[1], reverse=True))
    artist_bar_graph(dict_with_values_above_x(sorted_artist_dict, 3))


def printSong(songid):
    songinfo = sp.track(songid)
    print(songinfo)




# printPlaylists(brukernavn)
# printArtis(soilworkId)
#printPlaylist(spillelisteId)
# printSong(sangId)
