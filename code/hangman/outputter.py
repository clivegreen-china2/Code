import string
from math import floor
from colorama import Fore, Back, Style
from sys import stdout


class Outputter:
    display_width: int = 50
    bg_letters: str = Back.BLACK
    fg_invisible: str = Fore.BLACK
    bg_normal: str = Back.LIGHTBLACK_EX
    fg_normal: str = Fore.WHITE + '{}'
    fg_black: str = Fore.BLACK + '{}'
    fg_correct: str = Fore.GREEN + '{}'
    fg_incorrect: str = Fore.RED + '{}'
    fg_unchosen: str = Style.BRIGHT + Fore.LIGHTWHITE_EX + '{}'
    fg_faint: str = Style.DIM + Fore.LIGHTBLACK_EX
    start_piece: str = bg_letters + fg_invisible + '.'
    end_piece: str = start_piece + Style.RESET_ALL
    letter_separator: str = '  '

    @classmethod
    def colorize_letters(
            cls,
            letters: [str],
            correct: [str],
            incorrect: [str]
    ) -> str:

        colorized: [str] = []
        for c in letters:
            ansi_color: str = Outputter.fg_unchosen
            if c in correct:
                ansi_color = Outputter.fg_correct
            elif c in incorrect:
                ansi_color = Outputter.fg_incorrect
            colorized.append(ansi_color.format(c))

        colorized_letters = Outputter.letter_separator.join(colorized)
        return (
                Outputter.start_piece +
                colorized_letters +
                Outputter.end_piece
        )

    @classmethod
    def colorize_alphabet(cls, correct: [str], incorrect: [str]) -> str:
        alphabet: [str] = list(string.ascii_lowercase)
        row_1: [str] = alphabet[0:13]
        row_2: [str] = alphabet[13:]
        return (
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

        title_element: str = args.get('title', "<title>")
        padding: str = ' ' * 16
        title: str = f'{padding}{title_element}{padding}'
        title_formatted: str = (
            f"{(Outputter.bg_letters+Outputter.fg_correct).format(title)}"
            f"{Style.RESET_ALL}\n"
        )
        display_text += title_formatted

        info: str = args.get('info', '<info>')
        info_formatted: str = (
            f'{(Outputter.bg_normal+Outputter.fg_black).format(info)}'
            f'{Style.RESET_ALL}\n'
        )
        display_text += info_formatted

        canvas_element: [str] = args.get('canvas', '<canvas>')
        canvas_formatted: str = (
            f'{Outputter.bg_normal}{Outputter.fg_normal}'
            f'{''.join(canvas_element)}\n'
            f'{Style.RESET_ALL}\n'
        )
        display_text += canvas_formatted

        alphabet_formatted: str = Outputter.colorize_alphabet(
            args.get('correct', []),
            args.get('incorrect', [])
        )
        display_text += alphabet_formatted

        strap_element: str = args.get('strap', '<strap>')
        strap_formatted: str = (
            f'{Outputter.bg_normal}{Outputter.fg_normal}'
            f'{strap_element}\n'
            f'{Style.RESET_ALL}\n'
        )
        display_text += strap_formatted

        stdout.write("\r%s" % display_text)
        stdout.flush()
