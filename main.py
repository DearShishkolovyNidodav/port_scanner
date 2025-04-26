import socket
import termcolor

# Инициируем объект socket для установления соедтнения
sock = socket.socket()
# Устанавливаем соединение
sock.connect((ipaddress, port))