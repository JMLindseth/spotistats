from artists import artists_in_playlist, unique_artist_ids, all_artist_ids
from utils.dict_utils import sort_dict_desc
from pathlib import Path
from utils.graph import bar_graph
import json


def write_genres(genre_dict_list):
    Path("../out").mkdir(parents=True, exist_ok=True)
    with open('../out/genres.json', 'w') as convert_file:
        convert_file.write(json.dumps(genre_dict_list, indent=2))


def save_genres(total_genres, unique_artist_genres):
    sorted_genres_all = sort_dict_desc(total_genres)
    sorted_genres_unique = sort_dict_desc(unique_artist_genres)

    sorted_genres_all = {"name": "All artists", **sorted_genres_all}
    sorted_genres_unique = {"name": "Unique artists", **sorted_genres_unique}

    write_genres([sorted_genres_all, sorted_genres_unique])


def genres_for_artist(sp, artist_id):
    artist_info = sp.artist(artist_id)
    return artist_info['genres']


def genres_from_artist_list(sp, artists):
    genre_dict = {}

    for artist in artists:
        genre_list = genres_for_artist(sp, artist)

        for genre in genre_list:
            if genre in genre_dict:
                genre_dict[genre] += 1
            else:
                genre_dict[genre] = 1

    return genre_dict


def genres(sp, playlist_id):
    songs = sp.playlist(playlist_id)

    artists = artists_in_playlist(songs)
    len(artists)

    all_artists = all_artist_ids(artists)
    print(all_artists)

    unique_artists = unique_artist_ids(artists)
    print(unique_artists)
    print(len(unique_artists))

    genres_for_all_artists = genres_from_artist_list(sp, all_artists)
    genres_for_unique_artists = genres_from_artist_list(sp, unique_artists)

    save_genres(genres_for_all_artists, genres_for_unique_artists)

    return genres_for_all_artists, genres_for_unique_artists

def graph_genres(genres_dict, extra_text, filename):
    sorted_desc = sort_dict_desc(genres_dict)
    top_10 = dict(list(sorted_desc.items())[0:10])
    bar_graph(top_10, "Top 10 genres for unique artists", filename, extra_text)


def genre_stats(sp, playlist_id):
    all_artist_genres, unique_artis_genres = genres(sp, playlist_id)

    extra_text_unique = "For hver unike artist, finn alle sjangre og tell antall forekomster."
    extra_text_all = "For hver låt, finn alle sjangre til tilhørende artist og tell antall forekomster."

    graph_genres(unique_artis_genres, extra_text_unique, "unique_genres.png")
    graph_genres(all_artist_genres, extra_text_all, "all_genres.png")
