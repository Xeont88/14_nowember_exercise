from tkinter import *
from socket import *
import threading


class GUI_server(Tk):
    def __init__(self):
        super().__init__()
        self.sockobj = socket(AF_INET, SOCK_STREAM)
        self.sockobj.bind(('', 5400))
        self.sockobj.listen(5)

        self.text_space = Text()
        self.text_space.pack()

        print('start server')
        self.text_space.insert(END, 'start server\n')

        # создаем объект потока, с целью self.server_loop()
        server_thread = threading.Thread(target=self.server_loop)
        # установим поток как daemon по отношению к главному потоку
        server_thread.daemon = True
        # запустим поток сервера
        server_thread.start()

    def some_handler(self, msg):
        if self.str_data == 'привет':
            self.connection.send('Приветствую!'.encode('utf-8'))

        if self.str_data == 'пока':
            self.connection.send('Досвидания!'.encode('utf-8'))

        if self.str_data == 'спасибо':
            self.connection.send('Всегда пожалуйста!'.encode('utf-8'))

    def server_loop(self):
        while True:
            connection, address = self.sockobj.accept()  # ждем сообщение от клиента, устонавливаем соединение с клиентом, получаем ip адрес

            bin_data = connection.recv(1024)  # количество байтов
            str_data = bin_data.decode('utf-8')

            # TODO: Узнаем IP клиента,
            # создать словарь с привязкой имя: ip

            ip_addr = address[0]  # ip адрес

            print("Я получил сообщение:", str_data, ip_addr, '\n\n',)
            self.text_space.insert(END, "Я получил сообщение:"+str_data+ip_addr+'\n\n',)

            # self.some_handler(str_data)

            str_answer = 'сервер: ' + str_data + '\n' + 'Длинной ' + str(len(str_data))

            connection.send(str_answer.encode('utf-8'))
            connection.close()


gui_server = GUI_server()

gui_server.mainloop()
