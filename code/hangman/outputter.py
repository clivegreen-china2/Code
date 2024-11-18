from sys import stdout
from time import sleep
from colorama import Fore, Back, Style


# times: int = 10
# blank: str = ' '
# symbol: str = '|'
# cursor: str = f"\033[1;30;47m{symbol}"
#
# for i in range(times+1):
#     text: str = i * symbol
#     stdout.write("\r%s" % text + cursor)
#     stdout.flush()
#     sleep(0.5)


print(Back.BLACK + Fore.LIGHTRED_EX + ' A ' + Style.RESET_ALL, end=' ')
print(Back.LIGHTWHITE_EX + Fore.BLACK + ' B ' + Style.RESET_ALL, end=' ')
print(Back.BLACK + Fore.LIGHTGREEN_EX + ' C ' + Style.RESET_ALL, end=' ')
