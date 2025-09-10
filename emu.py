import shlex
vfs_name = "docker$ "
exit_cmd = "exit"

def act(a):
    parts = shlex.split(command)
    if command == exit_cmd:
        exit()
    if len(parts) == 0:
        return ""
    if parts[0] == 'ls':
        return parts
    elif parts[0] == 'cd':
        return parts
    else:
        return f'{command}: command not found'
if __name__ == "__main__":
    while True:
        command = input(vfs_name)
        print(act(command))