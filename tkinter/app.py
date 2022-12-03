from tkinter import *
from client import Client

import sys
import select

from threading import *


class PyChatApp():

    def __init__(self):
        self.client = Client()

        self.message = 'hello world!\n'
        self.app = Tk()
        self.app.title('PYCHAT')
        self.app.geometry('400x600')
        self.app.resizable(False, False)
        self.app.config(bg='#FFF')

        self.label_text = StringVar()
        self.label_text.set('Hello World!')

        # self.label = Label(textvariable=self.label_text, width=50, heigh=10, anchor=W, justify=RIGHT)
        # self.label.pack(expand=True)

        self.message_box = Text(self.app, width=400, heigh=20, wrap='word')
        self.message_box.pack(ipadx=0, ipady=0)
        self.message_box.insert('end', self.message)


        self.text_box = Text(self.app, width=400, heigh=10, wrap='word')
        self.text_box.pack(ipadx=0, ipady=0)
        self.text_box.insert('end', self.message)

        self.print_button = Button(self.app, text='Print', width=15, heigh=2, command=self.print_message)
        self.print_button.pack(ipadx=0, ipady=0, fill=BOTH, expand=True, side=LEFT)

        self.sync_button = Button(self.app, text='Sync', width=15, heigh=2, command=self.go_ahead())
        self.sync_button.pack(ipadx=0, ipady=0, fill=BOTH, expand=True, side=RIGHT)

        self.app.mainloop()

    def go_ahead(self):
        rcv = Thread(target=self.recive_message)
        rcv.start()

    def clear_text_box(self):
        self.text_box.delete(1.0, 'end')

    def print_message(self):
        mes = self.text_box.get(1.0, 'end')
        self.message_box.insert('end', '[YOU] ' + mes)
        self.text_box.delete(1.0, 'end')

        self.client.send_message(mes)

    def recive_message(self):
        while True:
            sockets_list = [sys.stdin, self.client.server]

            read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])

            for socks in read_sockets:
                if socks == self.client.server:
                     message = socks.recv(2048)
                     self.message_box.insert('end', message)
                     print(message)

app = PyChatApp()
app.run()
