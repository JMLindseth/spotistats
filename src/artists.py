from utils.dict_utils import dict_with_values_above_x, sort_dict_desc
from utils.graph import bar_graph


def all_artist_ids(artists):
    artist_ids = []

    for artist in artists:
        artist_ids.append(artist['id'])

    return artist_ids


def unique_artist_ids(artists):
    ids = all_artist_ids(artists)
    unique_artists = list(dict.fromkeys(ids))

    return unique_artists


def artist_names(artists):
    artist_dict = {}

    for artist in artists:
        artist_name = artist['name']

        if artist_name in artist_dict:
            artist_dict[artist_name] += 1
        else:
            artist_dict[artist_name] = 1

    return artist_dict


def artists_in_playlist(songs):
    artists = []

    for i, song in enumerate(songs['tracks']['items']):
        track = song['track']
        artists.append(track['artists'][0])

    return artists


def artist_bar_graph(artists_dict):
    top_artist_threshold = 3
    top_artists = dict_with_values_above_x(artists_dict, top_artist_threshold)
    title = f"Artists with > {top_artist_threshold} songs"
    filename = "top_artist.png"
    extra_text = f"Unique artists: {len(artists_dict)}"

    bar_graph(top_artists, title, filename, extra_text)


def artist_stats(sp, playlist_id):
    songs = sp.playlist(playlist_id)

    artists = artists_in_playlist(songs)

    artist_name_dict = artist_names(artists)
    sorted_artist_dict = sort_dict_desc(artist_name_dict)

    artist_bar_graph(sorted_artist_dict)
