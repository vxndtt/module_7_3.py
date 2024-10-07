from itertools import count
from operator import index
from os.path import split


class WordsFinder:
    def __init__(self, *names):
        self.file_names = names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    symbols = ',.=!?;:-'
                    for symbol in symbols:
                        line = line.replace(symbol, '')
                    words += line.split()
                all_words[file_name] = words

        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        word = word.lower()
        for key, value in all_words.items():
            if word in value:
                all_words[key] = value.index(word) + 1
                return all_words

    def count(self, word):
        all_words = self.get_all_words()
        word = word.lower()
        for key, value in all_words.items():
            count_ = value.count(word)
            all_words[key] = count_
            return all_words



finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))
