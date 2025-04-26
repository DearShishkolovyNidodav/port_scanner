import socket
import termcolor

# Пробуем подключиться к порту, если удалось то порт открыт, если нет - закрыт
def scan_port(ip_address, port):
    sock = socket.socket() # Инициируем объект socket для установления соединения
    sock.connect((ip_address, port)) # Устанавливаем соединение