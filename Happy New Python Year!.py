import colorama
from colorama import Fore

colorama.init()

# My Christmas tree
print(' ' * 39 + Fore.LIGHTRED_EX + '</>')
for i in range(1, 36):
    if i % 11 != 0:
        print(' ' * (40 - i) + Fore.GREEN + '*' * i + '|' + '*' * i)
    else:
        print(' ' * (41 - i) + Fore.LIGHTYELLOW_EX + 'Happy New Python Year!' * (i // 11))
