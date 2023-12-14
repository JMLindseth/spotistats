from utils.dict_utils import sort_dict_desc, dict_with_values_above_x
from utils.graph import bar_graph


def albums_bar_graph(albums_dict):
    top_album_threshold = 3
    top_artists = dict_with_values_above_x(albums_dict, top_album_threshold)
    title = f"Albums with > {top_album_threshold} songs"
    filename = "top_albums.png"
    extra_text = f"Unique albums: {len(albums_dict)}"

    bar_graph(top_artists, title, filename, extra_text)


def album_ranking(albums):
    album_dict = {}

    for album in albums:
        album_name = album['name']
        # album_name_and_artist = album_name + "(" + album['artists'][0]['name'] + ")"

        if album_name in album_dict:
            album_dict[album_name] += 1
        else:
            album_dict[album_name] = 1

    return album_dict


def albums_in_playlist(songs):
    albums = []

    for song in songs['tracks']['items']:
        track = song['track']
        albums.append(track['album'])

    return albums


def album_stats(sp, playlist_id):
    songs = sp.playlist(playlist_id)

    albums = albums_in_playlist(songs)

    album_ranks = album_ranking(albums)
    sorted_album_ranks = sort_dict_desc(album_ranks)

    albums_bar_graph(sorted_album_ranks)

