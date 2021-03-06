import socket
import sys


def call_echo_server(msg, buffsize=4096):
    #Set up the client socket.
    client_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_IP)

    client_socket.connect(('127.0.0.1', 50000))

    client_socket.sendall(msg)
    client_socket.shutdown(socket.SHUT_WR)

    done = False
    msg = ''
    while not done:
        msg_part = client_socket.recv(buffsize)
        if len(msg_part) < buffsize:
            done = True
        msg += msg_part

    client_socket.close()
    return msg


if __name__ == '__main__':
    if len(sys.argv) < 2:
        msg = raw_input("Enter your message.")
    else:
        msg = sys.argv[1]

    print(call_echo_server(msg, 32))
