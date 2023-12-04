import socket

# Configurar el cliente
host = '127.0.0.1'
port = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
# Enviar un mensaje al servidor
message = "Hola, servidor"
client.send(message.encode('utf-8'))
# Recibir la respuesta del servidor
response = client.recv(1024)
print(f"Respuesta del servidor: {response.decode('utf-8')}")

# Cerrar la conexión con el servidor
client.close()