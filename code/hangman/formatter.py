import math
from textwrap import TextWrapper

from colorizer import Colorizer
colorizer = Colorizer()
colorings = colorizer.colorings
colorize = colorizer.colorize




class Formatter:

    string_types: [str] = ['line', 'item']
    delimiters: dict[str: str] = dict(line='\n', item=' ')
    alignments: [str] = ['left', 'center']

    @classmethod
    def chunk_text(cls, text: str, max_chunk_length: int) -> [str]:

        return TextWrapper(max_chunk_length).wrap(text)
    
    @classmethod
    def select(
            cls,
            args: dict[str: str],
            key: str,
            default: str,
            allowed: [str]
    ):
        item = args.get_item(key, default)
        return item if item in allowed else default

    def __init__(self, **args):

        select = Formatter.select
        self.type = select(args, 'type', 'line', Formatter.string_types)

        self.style = select(
            args, 'style',
            Colorizer.default_style,
            Colorizer.styles.keys()
        )
        self.alignment = select(args, 'alignment', 'left', Formatter.alignments)
        self.delimiter = select(args, 'delimiter', '\n', Formatter.delimiters)

        self.text: str = args.get('text', '<TEXT MISSING>')
        self.max_text_width: int = args.get('max_text_width', len(self.text))
        self.indent: int = args.get('indent', 0)
        self.line_width = self.max_text_width + 2 * self.indent

        self.elements: [str] = TextWrapper(width=self.max_text_width).wrap(text=self.text)
        self.styled: str = ''

    def pad_elements(self) -> None:

        for index, element in enumerate(self.elements):

            if self.type == 'item':
                self.elements[index] = f'{self.indent * " "}{element}{self.indent * " "}'
            elif self.type == 'line':
                pad_width = self.line_width - len(element)
                l_pad_width: int = math.floor(pad_width/2) \
                    if self.alignment == 'center' else self.indent
                r_pad_width: int = pad_width - l_pad_width
                self.elements[index] = f'{l_pad_width * " "}{element}{r_pad_width * " "}'

    def stylize(self) -> None:
        ...

    def __str__(self):

        self.pad_elements()
        return self.delimiter.join(self.elements)


if __name__ == '__main__':
    ...
    f: Formatter = Formatter(
        text='HANGMAN',
        type='string',
        align='center',
        style='TITLE'
    )
