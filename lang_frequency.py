import os
import re
import collections


def input_way_to_filepath():
    way = input('Укажите путь к файлу:')
    if os.path.exists(way):
        return way


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as words:
            return words.read()


def get_most_frequent_words(text):
    words_text = re.sub(r'[^\w]', ' ', text).lower().split()
    repeated_words = collections.Counter(words_text).most_common(10)
    return repeated_words


if __name__ == '__main__':
    filepath = input_way_to_filepath()
    text = load_data(filepath)
    print(get_most_frequent_words(text))
