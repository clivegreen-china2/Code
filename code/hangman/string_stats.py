import re

class StringStats:
    def __init__(self, text_string: str):
        self.text_string_original = text_string
        self.word_list: [str] = re.findall(r'\w+', text_string.lower())
        self.word_count: int = len(self.word_list)
        self.word_lengths: [int] = [len(w) for w in self.word_list]
        self.text_string: str = ' '.join(self.word_list)
        self.all_letters_string: str = ''.join(self.word_list)
        self.all_letters_count: int = len(self.all_letters_string)
        self.all_letters_list: [str] = list(self.all_letters_string)
        self.unique_letters_list: [str] = sorted(list(set(self.all_letters_list)))
        self.unique_letters_count: int = len(self.unique_letters_list)
        self.letter_indices: dict[str:[int]] = {c: [] for c in self.unique_letters_list}
        for index, letter in enumerate(self.all_letters_list):
            self.letter_indices[letter].append(index)

    def __iter__(self):
        return iter([
            ('text_string_original', self.text_string_original),
            ('word_list', self.word_list),
            ('word_count', self.word_count),
            ('word_lengths', self.word_lengths),
            ('text_string', self.text_string),
            ('all_letters_string', self.all_letters_string),
            ('all_letters_count', self.all_letters_count),
            ('all_letters_list', self.all_letters_list),
            ('unique_letters_list', self.unique_letters_list),
            ('unique_letters_count', self.unique_letters_count),
            ('letter_indices', self.letter_indices)
        ])

    def show(self):
        [print(f'{pair[0]}: {pair[1]}') for pair in self]


text: str = 'Hangman is an AMAZING game!'
stats: StringStats = StringStats(text)
stats.show()

