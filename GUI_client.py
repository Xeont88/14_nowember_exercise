from tkinter import *
from socket import *


class Client(Tk):
    def __init__(self):
        super().__init__()
        self.config(bg='#111111')
        self.geometry('500x300')
        self.dialog_win = Text(self, width=40, height=15, background='darkgray')
        self.dialog_win.place(x=5, y=5)
        self.msg_space = Entry(self, width=35, bg='darkgray')
        self.msg_space.place(x=5, y=260)
        self.send_btn = Button(self, text='Отправить', bg='orange',
                               command=self.put_msg)
        self.send_btn.place(y=258, x=250)
        # self.socket_settings()
        self.server_address_lbl = Label(text='ip адрес сервера:',
                                        bg='#111111', fg='orange')
        self.server_address_lbl.place(x=340, y=15)
        self.server_address_entry = Entry(background='darkgray')
        self.server_address_entry.place(x=342, y=45)
        self.server_address_btn = Button(text='Установить', bg='orange',
                                         command=self.set_server_address)
        self.server_address_btn.place(x=395, y=75)

    def set_server_address(self):
        '''
        setting server address,
        and informing user about it
        :return:
        '''
        self.server_address = self.server_address_entry.get()
        self.print_text('Адрес сервера установлен '+self.server_address)

    def put_msg(self):
        text = self.msg_space.get()
        self.send_msg(text)
        self.msg_space.delete(0, END)

    def send_msg(self, msg):
        bin_msg = bytes(msg, 'utf-8')

        client = socket(AF_INET, SOCK_STREAM)
        try:
            server_address = (self.server_address, 5400)
            client.connect(server_address)
            client.sendall(bin_msg)
            data = client.recv(1024)
            self.print_text(data.decode('utf-8'))
        except:
            self.print_text('not connected')
        finally:
            client.close()

    def print_text(self, text):
        self.dialog_win.insert(END, text+'\n\n')


c = Client()
c.mainloop()
