import socket as s

HOST_SERVER = '127.0.0.1'
PORT_SERVER = 50001

with s.socket(s.AF_INET, s.SOCK_STREAM) as client:

    client.connect((HOST_SERVER, PORT_SERVER))

    client.send("Bom dia Servidor!")

    dataServer = client.recv(1024).decode('utf-8')

print(f"Dado recebido do servidor: {dataServer}")