import shlex
import os

vfs_name = os.getlogin()
exit_cmd = "exit"

def act(a):
    parts = shlex.split(a)
    if a == exit_cmd:
        exit()
    if len(parts) == 0:
        print("")
    if parts[0] == 'ls':
        p = os.listdir(path=".") # файлы в текущей директории
        print(p)
    elif parts[0] == 'cd':
        if len(parts) > 1:
            target_name = parts[1]
            if os.path.isdir(target_name):
                os.chdir(target_name)
            elif parts[1] == "$HOME":
                os.chdir(s)
            else:
                print(target_name)
        else:
            a = os.path.expanduser("~")
            os.chdir(a)
    elif parts[0] == 'pwd':
        print(os.getcwd())
    elif parts[0] == 'test':
        try:
            with open('test_fixed.txt', 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        print(f'{vfs_name}$ {line}')
                        act(line)
        except FileNotFoundError:
            print("test_fixed.txt: file not found")
    else:
        print(f'{command}: command not found')

if __name__ == "__main__":
    s = os.getcwd()  # текущая директория
    print(f'Текущая директория: {s}')
    while True:
        command = input(f'{vfs_name}$ ')
        act(command)