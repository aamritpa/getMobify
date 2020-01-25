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
            data = str(data)
            print('Data received %s' % data)

            connection.send(bytes('Got it!', 'utf8'))
        else:
            break

    connection.close()

def optimize_expression(expression):
    while True:
        result = expression.replace("++", "+")
        result = result.replace("--", "+")
        if result == expression: 
            return result
        expression = result


def validate_expression(expression):
    paranth_count = 0
    for c in expression:
        if c not in "+-*/ 0123456789.":
            return False
        if c == '(':
            paranth_count = paranth_count + 1
        if c == ')':
            paranth_count = paranth_count - 1
    if paranth_count != 0:
        return False
    return True
            

OPERATORS = "+-*/"

def parse_expression(expression):
    result_str = ''
    for c in expression:
        if (c >= '0' and c <= '9') or c == '.':
            result_str += c



    