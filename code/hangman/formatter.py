import math
from textwrap import TextWrapper
from styles import colorize


class Formatter:

    def __init__(self, **args):

        self.text: str = args.get('text', '<TEXT MISSING>')
        self.max_text_width: int = args.get('max_text_width', 43)
        self.pad_width: int = args.get('pad_width', 4)
        self.align: str = args.get('align', 'left')
        self.item_type: str = args.get('item_type', 'line')
        self.style: str = args.get('style', 'DEFAULT')
        self.delimiter: str = args.get('delimiter', '\n')

        self.frame_width = self.max_text_width + 2 * self.pad_width
        self.items: [str] = []
        self.dissect()

    def dissect(self) -> None:
        tw: TextWrapper = TextWrapper(width=self.max_text_width)
        self.items = tw.wrap(text=self.text)

    def pad_lines(self):
        ...

    def format(self) -> None:

        if self.item_type == 'line':
            tw: TextWrapper = TextWrapper(width=self.max_text_width)
            self.items: [str] = tw.wrap(text=self.text)
            for index, item in enumerate(self.items):
                pad_width: int = self.frame_width - len(item)
                l_pad_width: int = math.floor(pad_width/2) \
                    if self.align == 'center' else self.pad_width
                r_pad_width: int = pad_width - l_pad_width
                self.items[index] = f'{l_pad_width * " "}{item}{r_pad_width * " "}'
        else:
            self.items = list(self.text)
            pad: str = self.pad_width * ' '
            for index, item in enumerate(self.items):
                self.items[index] = f'{pad}{item}{pad}'


        colorize(self.items, self.style)

    def __str__(self):

        self.format()
        return self.delimiter.join(self.items)


if __name__ == '__main__':

    f: Formatter = Formatter(
        text='HANGMAN',
        align='center',
        style='TITLE'
    )
    print(f)

    f.text = 'Guess the word(s)!'
    print(f)

    f.text = ''
    f.style = 'NONE'
    print(f)

    # # ---------------
    #
    # f.item_type = 'character'
    # f.pad_width = 1
    # f.delimiter = ' '
    #
    # letters: [str] = []
    #
    # f.text = 'A'
    # f.style = 'CORRECT'
    # letters.append(f'{f}')
    #
    # f.text = 'B'
    # f.style = 'INCORRECT'
    # letters.append(f'{f}')
    #
    # f.text = 'C'
    # f.style = 'NORMAL'
    # letters.append(f'{f}')
    #
    # print(' '.join(letters))
    #
    # # ---------------
    #
    # f.text = ''
    # f.item_type = 'line'
    # f.style = 'NONE'
    # print(f)

    f.text = 'Type an available letter and hit the ENTER key:'
    f.align = 'left'
    f.style = 'NORMAL'
    print(f)


    f.item_type = 'character'
    f.pad_width = 1
    f.delimiter = ' '
    f.style = 'NORMAL'

    f.text = 'ABCDEFGHIJKLM'
    print(f)

    f.text = ''
    f.item_type = 'line'
    f.style = 'NONE'
    print(f)

    f.item_type = 'character'
    f.style = 'NORMAL'
    f.text = 'NOPQRSTUVWXYZ'
    print(f)
