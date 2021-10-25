from artists import artists_in_playlist, unique_artist_ids
from utils.dict_utils import sort_dict_desc


def genres_for_artist(sp, artist_id):
    artist_info = sp.artist(artist_id)
    return artist_info['genres']


def genres(sp, playlist_id):
    songs = sp.playlist(playlist_id)

    genre_dict = {}

    artists = artists_in_playlist(songs)
    len(artists)
    unique_artists = unique_artist_ids(artists)
    print(unique_artists)
    len(unique_artists)

    for artist in unique_artists:
        genre_list = genres_for_artist(sp, artist)

        for genre in genre_list:
            if genre in genre_dict:
                genre_dict[genre] += 1
            else:
                genre_dict[genre] = 1

    return genre_dict


def genre_stats(sp, playlist_id):
    genre_dict = genres(sp, playlist_id)
    sorted_genres = sort_dict_desc(genre_dict)

    print(sorted_genres)
