def dict_with_values_above_x(dictionary, x):
    filtered = {key: value for (key, value) in dictionary.items() if value > x}
    return filtered


def sort_dict_desc(dictionary):
    return dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))