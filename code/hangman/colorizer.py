from enum import Enum
from colorama import Fore, Back, Style
from collections import ChainMap


class Colorizer:

    __standard_colorings = dict(
        DEFAULT=Fore.LIGHTWHITE_EX+Back.BLACK,
        TITLE=Fore.BLACK+Back.LIGHTBLUE_EX,
        CORRECT=Fore.BLACK+Back.GREEN,
        INCORRECT=Fore.BLACK+Back.RED,
        DIMMED=Fore.LIGHTBLACK_EX+Back.BLACK
    )
    plain: str = Style.RESET_ALL

    @classmethod
    def colorize(cls, text: str, coloring: Enum) -> str:

        return f'{coloring.value}{text}{Colorizer.plain}'

    def __init__(self, custom_colorings: dict[str: str] = None):

        if custom_colorings is None:
            custom_colorings = {}

        # override standard colorings as needed:
        self.colors: ChainMap[str: str] = (
            ChainMap(custom_colorings, Colorizer.__standard_colorings)
        )
        self.colorings = Enum('Color', self.colors)


if __name__ == '__main__':

    customizations = dict(TITLE=Fore.BLACK+Back.LIGHTWHITE_EX)
    colorizer = Colorizer(customizations)
    colorings = colorizer.colorings
    colorize = colorizer.colorize

    the_text: str = '  Hello!  '
    the_coloring = colorings.TITLE
    print(
        colorize(the_text, the_coloring)
    )
