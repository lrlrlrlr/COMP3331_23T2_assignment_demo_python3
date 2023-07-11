import socket

def start_client():
    host = 'localhost'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        data = input('-> ')
        if not data:
            break
        client_socket.send(data.encode())

        data = client_socket.recv(1024).decode()
        print('Received from server: ' + data)

    client_socket.close()

if __name__ == '__main__':
    start_client()
