import os
from dotenv import load_dotenv
from artists import artist_stats
from genres import genre_stats
from albums import album_stats


load_dotenv()

PLAYLIST_ID = os.getenv('PLAYLIST_ID')


def generate_stats(sp):
    artist_stats(sp, PLAYLIST_ID)
    genre_stats(sp, PLAYLIST_ID)
    album_stats(sp, PLAYLIST_ID)
