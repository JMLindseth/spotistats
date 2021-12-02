from artists import artists_in_playlist, unique_artist_ids, all_artist_ids
from utils.dict_utils import sort_dict_desc


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

    return genres_for_unique_artists


def genre_stats(sp, playlist_id):
    genre_dict = genres(sp, playlist_id)
    sorted_genres = sort_dict_desc(genre_dict)

    print(sorted_genres)
