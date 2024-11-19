import string
from outputter import Outputter
from words import get_random_word as get_word
from string_stats import StringStats


class Hangman:
    alphabet: [str] = list(string.ascii_lowercase)
    max_incorrect: int = 11

    def __init__(self):
        self.stats: StringStats = StringStats(get_word())
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
                suffix: str = '' if count == 1 else ' {count} times'
                strap += f'was found{suffix}!\n'
            else:
                self.incorrect_letters.add(letter)
                strap += 'was not found.\n'

            if self.fully_guessed():
                strap = 'Congratulations :-) You did it!'
            elif self.guesses_remaining() == 0:
                strap = (
                    f'Commiserations :-( The correct answer is:\n'
                    f'{self.stats.text_string}.')
            else:
                gr: int = self.guesses_remaining()
                suffix: str = '' if gr == 1 else 'es'
                strap += (
                    f'You have {str(gr)} guess{suffix} remaining. '
                    f'Input another letter: '
                    )

        Outputter.output(
            info=self.stats.info,
            canvas=self.canvas,
            strap=strap,
            correct=self.correct_letters,
            incorrect=self.incorrect_letters
        )
