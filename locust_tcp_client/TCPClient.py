import socket


class TCPClient:
    def __init__(self):
        self.tcp = None

    def connect(self, hostname, port):
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp.connect((hostname, port))

    def disconnect(self):
        self.tcp.close()

    def send_socket_message(self, message):
        self.tcp.send(message)

    def receive_response(self):
        amount_received = 0
        response = None
        while amount_received == 0:
            response = self.tcp.recv(100)
            amount_received += len(response)
            print('Received "%s"' % response)
        return response

