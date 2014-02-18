import socket

#Set up the client socket.
client_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    socket.IPPROTO_IP)

client_socket.connect(('127.0.0.1', 50000))

msg = raw_input("Enter your message.")

client_socket.sendall(msg)
client_socket.shutdown(socket.SHUT_WR)

buffsize = 4096
done = False
msg = ''
while not done:
    msg_part = client_socket.recv(buffsize)
    if len(msg_part < buffsize):
        done = True
    msg += msg_part

print(msg)
client_socket.close()
