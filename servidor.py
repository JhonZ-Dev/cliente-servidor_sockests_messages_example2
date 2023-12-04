import socket
# Configurar el servidor
host = '127.0.0.1'
port = 12345
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)
print(f"Servidor escuchando en {host}:{port}")
# Esperar a que un cliente se conecte
client_socket, addr = server.accept()
print(f"Cliente conectado desde {addr[0]}:{addr[1]}")