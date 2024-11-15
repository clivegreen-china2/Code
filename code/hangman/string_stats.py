import re

class StringStats:
    def __init__(self, text_string: str):
        self.text_string_original = text_string
        self.word_list: [str] = re.findall(r'\w+', text_string.lower())
        self.text_string: str = ' '.join(self.word_list)
        self.word_count: int = len(self.word_list)
        self.word_lengths: [int] = [len(w) for w in self.word_list]
        self.letter_count = sum(self.word_lengths)
        self.unique_letters = sorted(list(set(''.join(self.word_list))))
        self.unique_letter_count = len(self.unique_letters)
        self.letter_indices: dict[str:[int]] = {c: [] for c in self.unique_letters}
        for index, letter in enumerate(self.text_string):
            self.letter_indices[letter].append(index)
