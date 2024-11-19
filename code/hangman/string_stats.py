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
        self.letter_indices: dict[str:[int]] = {c: [] for c in self.unique_letters}

        for i, c in enumerate(self.text_string):
            if c is not self.delimiter:
                self.letter_indices[c].append(i)

        self.delimiter_indices = [
            i for i,c in enumerate(self.text_string)
            if c == self.delimiter
        ]

        canvas: [str] = list('_' * self.text_string_length)
        for i in self.delimiter_indices:
            canvas[i] = '/'
        self.hangman_canvas: [str] = canvas

        suffix: str = '' if self.word_count == 1 else 's'
        self.info = (
            f'{self.word_count} word{suffix}; '
            f'{", ".join([str(n) for n in self.word_lengths])} letters'
        )

    def stats(self):
        return vars(self)

    def print(self) -> None:
        [
            print(f'{k}:\n{v}\n')
            for k, v in self.stats().items()
        ]


if __name__ == '__main__':
    text: str = 'Hangman can be a VERY educational game:-)'
    StringStats(text).print()
