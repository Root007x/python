import socket

HOST = '0.tcp.in.ngrok.io'  # The server's hostname or IP address
PORT = 18624        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)

print(data.decode('utf-8'))