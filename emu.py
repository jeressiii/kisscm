import shlex
import os

vfs_name = os.getlogin()
exit_cmd = "exit"

def act(a):
    parts = shlex.split(command)
    if command == exit_cmd:
        exit()
    if len(parts) == 0:
        return ""
    if parts[0] == 'ls':
        p = os.listdir(path=".") # файлы в текущей директории
        return p
    elif parts[0] == 'cd':
        if len(parts) > 1:
            if parts[1] == "$HOME":
                os.chdir(s)
            target_name = parts[1]
            current_path = os.getcwd()
            path_parts = current_path.split(os.sep) # делим директорию на части
            for i in range(len(path_parts)):
                if target_name == path_parts[i]:
                    target_path = os.sep.join(path_parts[:i + 1]) # обрезаем все после нашей директории
                    os.chdir(target_path)
                    if target_path == 'C:':
                        target_path += '\\'
                        os.chdir(target_path)
        return os.getcwd()
    else:
        return f'{command}: command not found'

if __name__ == "__main__":
    s = os.getcwd()  # текущая директория
    print(f'Текущая директория: {s}')
    while True:
        command = input(f'{vfs_name}$ ')
        print(act(command))