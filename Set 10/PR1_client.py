import socket

TCP_IP = '127.0.0.1'
TCP_PORT= 7007
BUFFER_SIZE = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
while True:
    data = input('\nClient:\n')
    if data == 'exit':break
    s.send(data.encode())
    data_bytes = s.recv(BUFFER_SIZE)
    received_data = data_bytes.decode()
    print('\nServer:\n{}'.format(received_data))
s.close()