from textwrap import TextWrapper

from code.hangman.palette import Palette


# from palette import Palette
# from colorama import Style


class Formatter:

    def __init__(self, **args):

        self.text_width: int = args.get('text_width', 80)
        self.pad_width = args.get('pad_width', 4)
        self.frame_width = self.text_width + 2 * self.pad_width

    def split_into_lines(self, text: str) -> [str]:
        return TextWrapper(width=self.text_width).wrap(text=text)

    def format_line(self, line: str, fore: str, back: str) -> str:
        ...





if __name__ == '__main__':

    formatter = Formatter()
    my_text = \
        'Hello there, and welcome to my wholly tedious, ' \
        'inconsequential and repetitious line of totally ' \
        'superfluous text, whose original length easily ' \
        'exceeds that of my stipulated maximum text width.'
    lines: [str] = formatter.split_into_lines(my_text)

    back: Palette = Palette.BACKGROUND

    [print(line) for line in lines]
