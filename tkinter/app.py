from tkinter import *


class PyChatApp():

    def __init__(self):
        self.message = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                          Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
                          Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
                          ``Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'''

        self.app = Tk()
        self.app.title('PYCHAT')
        self.app.geometry('400x500')
        self.app.resizable(False, False)
        self.app.config(bg='#FFF')

        self.label_text = StringVar()
        self.label_text.set('Hello World!')

        self.label = Label(textvariable=self.label_text, width=40, heigh=10, anchor=W, justify=RIGHT)
        self.label.pack(expand=True)

        self.text_box = Text(self.app, width=40, heigh=10, wrap='word')
        self.text_box.pack(expand=True)
        self.text_box.insert('end', self.message)

        self.clear_button = Button(self.app, text='Clear', width=15, heigh=2, command=self.clear_text_box)
        self.clear_button.pack(expand=True)

        self.print_button = Button(self.app, text='Print', width=15, heigh=2, command=self.print_text_label)
        self.print_button.pack(expand=True)


    def run(self):
        try:
            self.app.mainloop()
        except Exception as e:
            print(e)


    def clear_text_box(self):
        self.text_box.delete(1.0, 'end')
        self.label_text.set('')


    def print_text_label(self):
        self.label_text.set(self.text_box.get(1.0,'end'))

app = PyChatApp().run()
