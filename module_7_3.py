from os.path import split


class WordsFinder():
    def __init__(self, *names):
        self.file_names = []
        for name in names:
            self.file_names.append(name)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    symbols = ',.=!?;:-'
                    for symbol in symbols:
                        line = line.replace(symbol, '')
                    words = line.split()
                    print(words)
                all_words = dict.fromkeys(file_name, words)
                return all_words

    #def find(self, word):
        #dict = {}




finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
#print(finder2.find('TEXT')) # 3 слово по счёту
#print(finder2.count('teXT')) # 4 слова teXT в тексте всего

#symbols = [',', '.', '=', '!', '?', ';', ':', ' - ']
#for symbol in symbols:
    #line = line.replace(symbol, '')