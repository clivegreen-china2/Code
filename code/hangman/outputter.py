import string
from math import floor
from colorama import Fore, Back, Style
# from sys import stdout

# stdout.write("\r%s" % text + cursor)
# stdout.flush()


class Outputter:
    bg_color: str = Back.BLACK
    fg_invisible: str = Fore.BLACK
    fg_correct: str = Fore.GREEN + '{}'
    fg_incorrect: str = Fore.RED + '{}'
    fg_unchosen: str = Style.BRIGHT + Fore.LIGHTWHITE_EX + '{}'
    fg_faint: str = Style.DIM + Fore.LIGHTBLACK_EX

    start_piece: str = bg_color + fg_invisible + '.'
    end_piece: str = start_piece + Style.RESET_ALL
    separator: str = fg_faint + ' | '

    @classmethod
    def output(cls, **args) -> str:
        pass

    @classmethod
    def alphabet(cls, correct: [str], incorrect: [str]) -> str:

        colorized: [str] = []
        for c in string.ascii_lowercase:
            ansi: str = Outputter.fg_unchosen
            if c in correct:
                ansi = Outputter.fg_correct
            elif c in incorrect:
                ansi = Outputter.fg_incorrect
            colorized.append(ansi.format(c))

        alpha_string = Outputter.separator.join(colorized)
        fold_index: int = floor(len(alpha_string) / 2)
        alpha_string = (
                alpha_string[0:fold_index+1] + '\n' +
                alpha_string[fold_index:])

        return (
            Outputter.start_piece +
            alpha_string +
            Outputter.end_piece
        )
