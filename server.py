import socket

HOST = 'localhost'  # Standard loopback interface address (localhost)
PORT = 9999        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('Waiting for a connection...')
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        msg = input("Enter any msg: ")
        conn.sendall(bytes(msg,'utf-8'))

