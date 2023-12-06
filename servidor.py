import socket

# Configurar el servidor
host = '127.0.0.1'  # Dirección IP en la que el servidor está escuchando
port = 12345  # Puerto en el que el servidor está escuchando
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlace y escucha
server.bind((host, port))
server.listen(5)  # Se permite un máximo de 5 conexiones en espera
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
print(f"Respuesta enviada al cliente: {response}")

# Cerrar la conexión con el cliente
client_socket.close()

# Cerrar el socket del servidor
server.close()
print("Conexiones cerradas")
