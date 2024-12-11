from colorama import Fore, Back, Style


d = dict
default_style: d[str:str] = d(
    fg=Fore.LIGHTWHITE_EX,
    bg=Back.BLACK
)


def make_pair(args: d[str:str]) -> d[str:str]:
    customized: d[str: str] = default_style.copy()
    customized.update(args)
    return customized


styles: d[str: d[str:str]] = d(

    DEFAULT=default_style,
    NONE=d(fg=Style.RESET_ALL, bg=''),
    TITLE=d(fg=Fore.BLACK, bg=Back.LIGHTBLUE_EX),
    CORRECT=make_pair(d(fg=Fore.BLACK, bg=Back.GREEN)),
    INCORRECT=make_pair(d(fg=Fore.BLACK, bg=Back.RED)),
    DIMMED=make_pair(d(fg=Fore.LIGHTBLACK_EX))
)


def colorize(items: [str], style: str) -> None:

    colors = styles.get(style, default_style)
    pre: str = colors['fg'] + colors['bg']
    post: str = styles['NONE']['fg']

    for index, line in enumerate(items):
        items[index] = f'{pre}{line}{post}'
