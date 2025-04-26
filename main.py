import socket
import termcolor

# Запускаем функцию scan_port для каждого отдельного порта
def scan(target, ports):
    global open_port, close_port
    open_port = 0
    close_port = 0
    print(termcolor.colored(('\n' + f'Начало сканирование для цели {target}'), 'yellow'))
    for port in range(0, ports):
        scan_port(target, port)

# Пробуем подключиться к порту, если удалось то порт открыт, если нет - закрыт:
def scan_port(ip_address, port):
    global open_port, close_port
    try:
        sock = socket.socket() # Инициируем объект socket для установления соединения
        sock.connect((ip_address, port)) # Устанавливаем соединение
        print(termcolor.colored((f"[+] Порт {port} открыт"), 'green'))
        open_port += 1
        sock.close()
    except:
        close_port += 1
        if hide_close == 0:
            print(termcolor.colored((f"[-] Порт {port} закрыт"), 'red'))
        else:
            pass

# Счетчики открытых и закрытых портов
open_port = 0
close_port = 0

# Скрывать ли закрытые порты:
hide_close = 0

# Входные данные
targets = input(termcolor.colored(("[*] Введите цели для сканирования (через запятую): "), 'blue'))
ports = int(input(termcolor.colored(("[*] Введите количество портов для сканирования: "), 'blue')))
hide_close = int(input(termcolor.colored(("Скрывать ли закрытые порты (0 - нет, 1 - да): "), 'blue')))
# Определяем, одну или множество целей необходимо просканировать:
if ',' in targets:
    print(termcolor.colored(("[*] Сканирование множества целей: "), 'yellow'))
    for ip_addr in targets.split(','):  # Разделяем ip адреса целей и сканируем по очереди
        scan(ip_addr.strip(' '), ports)
        print(termcolor.colored((f"Портов открыто: {open_port}, портов закрыто: {close_port}"), 'yellow'))
else:
    scan(targets, ports) # Иначе сканируем только одну цель
    print(termcolor.colored((f"Портов открыто: {open_port}, портов закрыто: {close_port}"), 'yellow'))