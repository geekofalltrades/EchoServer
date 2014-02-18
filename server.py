import socket

#Set up the server socket.
server_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    socket.IPPROTO_IP)

server_socket.bind(('127.0.0.1', 50000))
server_socket.listen(1)

#Loop indefinitely while waiting for connections.
while True:
    conn, addr = server_socket.accept()
    buffsize = 4096
    done = False
    msg = ''
    while not done:
        msg_part = conn.recv(buffsize)
        if len(msg_part) < buffsize:
            done = True
        msg += msg_part

    conn.shutdown(socket.SHUT_RD)
    conn.sendall(msg)
    conn.shutdown(socket.SHUT_WR)
    conn.close()
