import os
import sys

import socket
from contextlib import closing


def check_socket(port):
    host = '127.0.0.1'
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        return not sock.connect_ex((host, port)) == 0


port = int(sys.argv[1])
os.system('python3.10 kill.py')

print('Запускаем бота...')
if not check_socket(port):
    print('Порт занят')
    os.system('python3.10 kill.py')
    exit(0)

os.system('cd bot && nohup python3.10 main.py > bot.log &')
os.system(f'cd server && nohup python3.10 manage.py runserver 0.0.0.0:{port} > server.log &')
os.system('cd server && nohup python3.10 manage.py qcluster > qluster.log &')

print('Бот запустился')
print(f'Админ-панель запустился запустился на порте {port}')
