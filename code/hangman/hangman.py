import string
from outputter import Outputter
from words import get_random_word
from string_stats import StringStats


class Hangman:
    alphabet: [str] = list(string.ascii_lowercase)
    max_incorrect: int = 11

    def __init__(self, text: str = get_random_word()):
        self.stats: StringStats = StringStats(text)

        self.valid_letters: [str] = self.stats.unique_letters
        self.letter_indices = self.stats.letter_indices
        self.selectable_letters: [str] = Hangman.alphabet.copy()

        self.correct_letters: set[str] = set()
        self.incorrect_letters: set[str] = set()

        self.correct_guesses = lambda: (
            len(self.correct_letters)
        )
        self.incorrect_guesses = lambda: (
            len(self.incorrect_letters)
        )
        self.guesses_remaining = lambda: (
                Hangman.max_incorrect -
                self.incorrect_guesses() + 1
        )
        self.fully_guessed = lambda: (
                self.correct_guesses ==
                self.stats.unique_letter_count
        )
        self.canvas: [str] = list(self.stats.hangman_canvas)
        self.info: str = self.stats.info
        self.strap: str = ''

    def guess(self, letter: str) -> None:

        strap: str = f'The letter \'{letter}\' '

        if letter not in self.selectable_letters:
            strap += 'has already been used.\n'
        else:
            self.selectable_letters.remove(letter)
            if letter in self.valid_letters:
                self.correct_letters.add(letter)
                indices: [int] = self.letter_indices[letter]
                for i in indices:
                    self.canvas[i] = letter
                count = len(indices)
                suffix: str = \
                    '' if count == 1 else f' {count} times'
                self.strap += f'was found{suffix}!\n'
            else:
                self.incorrect_letters.add(letter)
                self.strap += 'was not found.\n'

            if self.fully_guessed():
                self.strap = 'Congratulations :-) You did it!'
            elif self.guesses_remaining() == 0:
                self.strap = (
                    f'Commiserations :-( The answer is:\n'
                    f'{self.stats.text}.')
            else:
                gr: int = self.guesses_remaining()
                suffix: str = '' if gr == 1 else 'es'
                self.strap += (
                    f'{str(gr)} guess{suffix} remaining. '
                    f'Type a letter and hit ENTER: '
                    )
            self.output()

    def output(self):
        Outputter.output(
            title='HANGMAN',
            info=self.stats.info,
            canvas=self.canvas,
            strap=self.strap,
            correct=self.correct_letters,
            incorrect=self.incorrect_letters
        )
