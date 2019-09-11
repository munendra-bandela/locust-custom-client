import socket
# import StringIO

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('TCP HOST', 7564))

print(client.getpeername())

try:
    # Send data
    message = chr(0x02) + 'tcp message' + chr(0x03)
    client.send(message.encode())

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received == 0:
        data = client.recv(100)
        amount_received += len(data)
        print('received "%s"' % data)

finally:
    print('closing client')
    client.close()
