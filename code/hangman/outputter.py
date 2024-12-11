import string
from math import floor
from formatter import Formatter
from sys import stdout


class Outputter:

    @classmethod
    def colorize_alphabet(cls, correct: [str], incorrect: [str]) -> str:

        letters: [str] = list(string.ascii_lowercase)
        length: int = len(letters)
        count: int = int(length / 2)
        part1: slice = slice(0, count)  # index values: 0 to count-1
        part2: slice = slice(count)  # index values: count to length-1

        row_1, row_2 = letters[part1], letters[part2]
        return (

            Formatter(
                text='Guess the word(s)!',
                align='center',
                style='NORMAL'
            )



            f'{Outputter.colorize_letters(row_1, correct, incorrect)}\n'
            f'{Outputter.colorize_letters(row_2, correct, incorrect)}'
        )

    @classmethod
    def pad_out(cls, text: str) -> str:
        diff: int = Outputter.display_width - len(text)
        if diff <= 0:
            return text
        if diff % 2 > 0:
            text += ' '
            diff -= 1

        pad_width: int = floor(diff / 2)
        pad: str = pad_width * ' '
        return pad + text + pad

    @classmethod
    def output(cls, **args) -> None:
        display_text: str = ''

        title: str = Outputter.pad_out(args.get('title', "<title>"))
        title_formatted: str = (
            f"{(Outputter.bg_letters+Outputter.fg_correct).formatted(title)}"
            f"{Style.RESET_ALL}\n"
        )
        display_text += title_formatted

        info: str = Outputter.pad_out(args.get('info', '<info>'))
        info_formatted: str = (
            f'{(Outputter.bg_normal+Outputter.fg_black).formatted(info)}'
            f'{Style.RESET_ALL}\n'
        )
        display_text += info_formatted

        canvas_characters: [str] = args.get('canvas', [])
        canvas: str = Outputter.pad_out(''.join(canvas_characters))
        canvas_formatted: str = (
            f'{Outputter.bg_normal}{Outputter.fg_normal}'
            f'{''.join(canvas)}\n'
            f'{Style.RESET_ALL}\n'
        )
        display_text += canvas_formatted

        alphabet_formatted: str = Outputter.pad_out(Outputter.colorize_alphabet(
            args.get('correct', []),
            args.get('incorrect', [])
        ))
        display_text += alphabet_formatted

        strap_element: str = Outputter.pad_out(args.get('strap', '<strap>'))
        strap_formatted: str = (
            f'{Outputter.bg_normal}{Outputter.fg_normal}'
            f'{strap_element}\n'
            f'{Style.RESET_ALL}\n'
        )
        display_text += strap_formatted

        stdout.write("\r%s" % display_text)
        stdout.flush()


if __name__ == '__main__':
    pass
