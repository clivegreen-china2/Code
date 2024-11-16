import string
from words import get_random_word as get_word
from string_stats import StringStats


class Hangman:
    max_incorrect: int = 11

    def __init__(self):
        self.stats = StringStats(get_word())
        self.correct_letters: [str] = []
        self.incorrect_letters: [str] = []

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
        self.prompt = lambda: (
            f'Select a letter ({self.guesses_remaining()}'
            f' guess{'' if self.guesses_remaining() == 1 else'es'}'
            f' remaining):'
        )

        self.canvas = ' ' * self.stats.text_string_length
        self.alpha_string = string.ascii_lowercase
