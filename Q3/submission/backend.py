import numpy as np
import socket
import os

SOCKET_FILE = '/tmp/q3-mobify'

try:
    os.unlink(SOCKET_FILE)
except OSError:
    if os.path.exists(SOCKET_FILE):
        raise

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
print('Binding socket')
sock.bind(SOCKET_FILE)
sock.listen(1)

while True:
    connection, port = sock.accept()
    print('Connection from %s' % port)
    while True:
        data = connection.recv(256)
        if data:
            data = data.decode('utf-8')
            print('Data received %s' % data)
            try:
                result = str(eval(data))
            except:
                result = 'Invalid!'
            connection.send(bytes(result, 'utf8'))
        else:
            break

    connection.close()


    