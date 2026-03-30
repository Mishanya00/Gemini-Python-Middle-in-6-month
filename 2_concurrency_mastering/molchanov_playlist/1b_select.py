import socket
from select import select


to_monitor = dict()


def accept_connection(server_socket):
    client_socket, client_address = server_socket.accept()
    print('Connection from', client_address)

    to_monitor[client_socket] = send_message


def send_message(client_socket):
    request = client_socket.recv(4096)

    if request:
        response = 'Hello, world!\n'.encode()
        client_socket.send(response)
    else:
        client_socket.close()
        del to_monitor[client_socket]


def event_loop():
    while True:
        ready_to_read, _, _ = select(to_monitor.keys(), [], []) # read, write, errors

        for sock in ready_to_read:
            to_monitor[sock](sock)


if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    to_monitor[server_socket] = accept_connection

    event_loop()