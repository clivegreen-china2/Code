import re

class StringStats:
    def __init__(self, text_string: str):
        self.text_string_original: str = text_string
        self.delimiter: str = ' '
        self.word_list: [str] = re.findall(r'\w+', text_string.lower())
        self.text_string: str = self.delimiter.join(self.word_list)
        self.text_string_length: int = len(self.text_string)
        self.word_count: int = len(self.word_list)
        self.word_lengths: [int] = [len(w) for w in self.word_list]
        self.letter_count = sum(self.word_lengths)
        self.unique_letters: [str] = sorted(list(set(''.join(self.word_list))))
        self.unique_letter_count: int = len(self.unique_letters)
        self.letter_indices: dict[str:[int]] = dict(zip(self.unique_letters, list()))
        for i, c in enumerate(self.text_string):
            if c is not self.delimiter:
                self.letter_indices[c].append(i)
