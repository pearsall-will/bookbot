from collections import Counter, OrderedDict

class book:

    def __init__(self, book):
        self.book_path = f'books/{book}.txt'
        self.book_data = None
        self.letter_counts = None
        self.word_count = None

    def read(self):
        if self.book_data is not None:
            return
        with open(self.book_path, 'r') as f:
            self.book_data = f.read()

    def count_words(self):
        self.read()
        if self.word_count is not None:
            return
        self.word_count = len(self.book_data.split())

    def count_letters(self):
        self.read()
        if self.letter_counts is not None:
            return
        self.letter_counts = dict(sorted(Counter(self.book_data.lower()).items(), key=lambda x: x[1], reverse=True))

    def print_report(self):
        self.count_words()
        self.count_letters()
        print(f'--- Begin report of {self.book_path} ---')
        print()
        print(f'Word count: {self.word_count}')
        print('Letter Counts')
        for letter in self.letter_counts:
            if not letter.isalpha():
                continue
            print(f'\t{letter}: {self.letter_counts[letter]}')
        print()
        print('--- End report ---')

def main():
    frankenstein = book('frankenstein')
    frankenstein.print_report()

if __name__=='__main__':
    main()
