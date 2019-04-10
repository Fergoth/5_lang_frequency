import sys
from collections import Counter
import re


def load_data(filepath):
    with open(filepath, encoding='utf-8') as file:
        text = file.read()
        return text


def get_most_frequent_words(text, n_first_words=10):
    words = re.findall(r'\w+', text)
    return Counter(words).most_common(n_first_words)


def print_counter(count_object):
    print('{:^20} {:^10}'.format('Слово', 'Частота'))
    print('_'*30)
    for word, freq in count_object:
        print('{:^20}|{:^10}'.format(word, freq))


if __name__ == '__main__':
    try:
        path = sys.argv[1]
        text_from_file = load_data(path)
    except IndexError:
        sys.exit('Требуется путь к файлу как аргумент')
    except FileNotFoundError:
        sys.exit('Файл не найден')
    words_counter = get_most_frequent_words(text_from_file)
    print_counter(words_counter)
