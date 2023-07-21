import socket
import json
def start_server():
    host = 'localhost'
    port = 12347

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))

    server_socket.listen(1)
    print('Server is listening on port', port)

    conn, address = server_socket.accept()
    print('Connection from', address)

    while True:
        data = conn.recv(1024).decode()
        loaded_data = json.loads(data)
        print(type(data))
        print(type(loaded_data))
        if not data:
            break
        print('Received from client: ' + data)

        data = "This is the reply from server (replace it)"
        conn.send(data.encode())

    conn.close()

if __name__ == '__main__':
    start_server()