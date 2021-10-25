import matplotlib.pyplot as plt


def bar_graph(dictionary, title):
    fig = plt.figure()
    ax = fig.add_subplot(211)
    names = dictionary.keys()
    num_songs = dictionary.values()
    ax.bar(names, num_songs)
    plt.xticks(rotation=90)
    plt.title(title)
    plt.show()
