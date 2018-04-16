import socket

TCP_IP = '127.0.0.1'
TCP_PORT= 7007
BUFFER_SIZE = 5000

data = input("Enter elements to sort: ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(data.encode())
data_bytes = s.recv(BUFFER_SIZE)
data = data_bytes.decode()
s.close()
print("sorted data: {}".format(data.split()))