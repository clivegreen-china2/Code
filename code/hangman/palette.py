import enum
from colorama import Fore, Back


class Palette(enum):
        TITLEBAR: Back.LIGHTBLACK_EX
        BACKGROUND: Back.BLACK
        TEXT_TITLE: Fore.BLACK
        TEXT_NORMAL: Fore.LIGHTWHITE_EX
        TEXT_DIMMED: Fore.LIGHTBLACK_EX
        TEXT_CORRECT: Fore.GREEN
        TEXT_INCORRECT: Fore.RED

