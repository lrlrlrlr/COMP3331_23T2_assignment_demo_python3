import socket

class InvalidURL(Exception):
    pass

def start_server():
    host = 'localhost'
    port = 12346

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))

    server_socket.listen(1)
    print('Server is listening on port', port)

    conn, address = server_socket.accept()
    print('Connection from', address)

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break


        if data == "www.xexample.com":
            raise InvalidURL

        print('Received from client: ' + data)

        data = "This is the reply from server (replace it)"
        conn.send(data.encode())

    conn.close()

if __name__ == '__main__':
    try:
        start_server()
    except KeyboardInterrupt:
        print("user stopped the client!")

    # if ... is None:
        # todo

    except InvalidURL:
        print("Invalid URL!")

    except Exception as E:
        print(f"unknown error: {E}:{E.args}")

