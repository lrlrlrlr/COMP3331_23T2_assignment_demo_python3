import socket

def start_client():
    host = 'localhost'
    port = 12346

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
    try:
        start_client()
    except KeyboardInterrupt:
        print("user stopped the client!")
    except Exception as E:
        print(f"unknown error: {E}:{E.args}")

