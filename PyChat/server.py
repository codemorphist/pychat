import socket
import _thread
from config import HOST, PORT

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))

server.listen(100)

clients_list = []


def client_thread(conn, addr):
   '''
   Function create thread and handle client messages
   '''
   message = ''
   while True:
      try:
         message = conn.recv(2048)
         if message:
            message = f'[{addr[0]}:{addr[1]}] {message.decode()}'
            print(message)
            broadcast(message, conn, addr)
         else:
            remove(conn)
      except Exception as ex:
         print(ex)
         continue


def broadcast(message, conn, addr):
   '''
   Function send new message to clients
   '''
   for client in clients_list:
      if client[0] != conn:
         try:
            client[0].send(message.encode())
            print(f'[SUCCESS] Message send to {addr[0]}:{addr[1]} !')
         except Exception as ex:
            print(ex)
            client.close()
            remove(conn)


def remove(conn):
   '''
   Function remove client from client_list
   if them is inactive, or disconected
   '''
   if conn in client_list:
      clients_list.remove(conn)
      print('[ERROR] Client was removed, connection was closed.')


while True:
   conn, addr = server.accept()
   print(f'[SUCCESS] Connected from: {addr[0]}:{addr[1]}')
   clients_list.append((conn, addr))

   _thread.start_new_thread(client_thread, (conn, addr))

conn.close()
server.close()
