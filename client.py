import socket
from config import HOST, PORT

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(''.encode())

    while True:
        message = ''
        message = input('YOU: ')

        if message == 'exit':
            break

        s.sendall(message.encode())

        data = s.recv(1024)

        if data:
            print('SERVER: ', data.decode())

    s.close()
