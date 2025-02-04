import re


class StringStats:

    def __init__(self, text: str):

        self.text_original: str = text
        self.words: [str] = re.findall(r'\w+', text.lower())
        self.word_delimiter: str = ' '
        self.text: str = self.word_delimiter.join(self.words)
        self.text_length: int = len(self.text)

        self.word_count: int = len(self.words)
        self.word_lengths: [int] = [len(w) for w in self.words]

        self.letter_count = sum(self.word_lengths)
        self.unique_letters: [str] = sorted(list(set(''.join(self.words))))
        self.unique_letter_count: int = len(self.unique_letters)

        self.delimiter_indices: [int] = []
        self.letter_indices: dict[str:[int]] = {}

        for i, c in enumerate(self.text):
            if c is self.word_delimiter:
                self.delimiter_indices.append(i)
            else:
                indices: [int] = self.letter_indices.get(c, [])
                indices.append(i)
                self.letter_indices.update({c:indices})

        self.blank_canvas: [str] = list('_' * self.text_length)
        for i in self.delimiter_indices:
            self.blank_canvas[i] = '/'

        suffix: str = '' if self.word_count == 1 else 's'
        self.info = (
            f'{self.word_count} word{suffix} '
            f'({",".join([str(n) for n in self.word_lengths])})'
        )

    def stats(self) -> dict:

        return vars(self)

    def print(self) -> None:
        [
            print(f'{k}:\n{v}\n')
            for k, v in self.stats().items()
        ]
