import socket
from config import HOST, PORT

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
   s.bind((HOST, PORT))
   s.listen(1)
   conn, addr = s.accept()

   with conn:
       print('Connected by: ', addr)
       conn.send(''.encode())

       while True:
           message = ''
           message = input('YOU: ')

           if message == 'exit':
              break

           conn.sendall(message.encode())

           data = conn.recv(1024)

           if data:
               print('CLIENT: ', data.decode())
   conn.close()
   s.close()
