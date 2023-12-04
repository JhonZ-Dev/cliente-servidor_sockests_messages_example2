import socket

# Configurar el cliente
host = '127.0.0.1'
port = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
# Enviar un mensaje al servidor
message = "Hola, servidor"
client.send(message.encode('utf-8'))