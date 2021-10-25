from spotipySetup import init_spotipy
from stats import generate_stats


def main():
    sp = init_spotipy()
    generate_stats(sp)


main()
