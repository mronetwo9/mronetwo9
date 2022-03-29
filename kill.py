import psutil
import os

curdir = os.path.dirname(__file__)
for proc in psutil.process_iter():
    if proc.cwd().startswith(curdir) and 'python3.10' in proc.cmdline()[0]:
        if proc.cmdline()[1] not in ['run.py', 'kill.py']:
            print(proc.cmdline())
            proc.kill()

print('Отключаем бота...')
print('Бот выключено')
