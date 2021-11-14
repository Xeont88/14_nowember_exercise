from socket import *

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind(('', 5400))
sockobj.listen(5)


def some_handler(msg):
    if str_data == 'привет':
        connection.send('Приветствую!'.encode('utf-8'))

    if str_data == 'пока':
        connection.send('Досвидания!'.encode('utf-8'))

    if str_data == 'спасибо':
        connection.send('Всегда пожалуйста!'.encode('utf-8'))


while True:
    connection, address = sockobj.accept()  # ждем сообщение от клиента, устонавливаем соединение с клиентом, получаем ip адрес

    bin_data = connection.recv(1024)  # количество байтов
    str_data = bin_data.decode('utf-8')

    # TODO: Узнаем IP клиента,
    # создать словарь с привязкой имя: ip

    ip_addr = address[0]  # ip адрес

    print("Я получил сообщение:", str_data, ip_addr, '\n\n',)

    some_handler(str_data)

    str_answer = 'я (сервер) получил: ' + str_data + '\n' + 'Длинной ' + str(len(str_data)) + ' байт'

    connection.send(str_answer.encode('utf-8'))
    connection.close()
