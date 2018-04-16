import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 7007
BUFFER_SIZE = 5000
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
conn, addr = s.accept()
while 1:
    data_bytes = conn.recv(BUFFER_SIZE)
    data = data_bytes.decode()
    if not data: break
    print("Received Data:{}".format(data))
    data_list = data.split()
    data_list.sort()
    data_to_send = ' '.join(data_list)
    conn.send(data_to_send.encode())
    print("Data sent:{}".format(data_list))
conn.close()