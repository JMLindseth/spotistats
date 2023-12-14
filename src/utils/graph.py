import matplotlib.pyplot as plt
from pathlib import Path


def save_graph_file(filename):
    Path("../out").mkdir(parents=True, exist_ok=True)
    plt.savefig("../out/" + filename, dpi=500)


def annotate_with_number_of_songs(names, num_songs):
    for x, y in zip(names, num_songs):
        plt.annotate(y,
                     (x, y),
                     textcoords="offset points",
                     xytext=(0, 10),
                     ha='center')


def bar_graph(dictionary, title, filename, extra_text):
    fig = plt.figure()
    ax = fig.add_subplot(211)
    names = dictionary.keys()
    num_songs = dictionary.values()
    ax.bar(names, num_songs)
    plt.xticks(rotation=45, ha="right")
    plt.title(title)
    plt.gcf().text(0.09, 0.1, extra_text, fontsize=10)

    annotate_with_number_of_songs(names, num_songs)

    save_graph_file(filename)
