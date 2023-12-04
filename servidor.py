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
# Recibir datos del cliente
data = client_socket.recv(1024)
print(f"Mensaje recibido del cliente: {data.decode('utf-8')}")

# Responder al cliente
response = "Mensaje recibido correctamente"
client_socket.send(response.encode('utf-8'))
# Cerrar la conexión con el cliente y el servidor
client_socket.close()
server.close()