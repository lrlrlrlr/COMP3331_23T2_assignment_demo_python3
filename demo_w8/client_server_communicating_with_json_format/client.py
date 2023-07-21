import socket
import json



def start_client():
    host = 'localhost'
    port = 12347

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        data = input('-> ')
        message = {"ts": 11123232, "data": data, "info1": "info"}
        message = json.dumps(message) # convert dict to strings
        if not data:
            break
        client_socket.send(message.encode()) # .encode() convert strings to bytes

        data = client_socket.recv(1024).decode()
        print('Received from server: ' + data)

    client_socket.close()

if __name__ == '__main__':
    start_client()