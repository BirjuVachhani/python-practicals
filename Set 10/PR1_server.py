import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 7007
BUFFER_SIZE = 5000
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
conn, addr = s.accept()
while True:
    data_bytes = conn.recv(BUFFER_SIZE)
    data = data_bytes.decode()
    if not data: break
    if data == 'exit': break
    print("Client\n{}\n".format(data))
    data_to_send = input("Server:\n")
    conn.send(data_to_send.encode())
conn.close()